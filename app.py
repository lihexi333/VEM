from flask import Flask, render_template, request, session, jsonify
from beverage import Beverage, Coca, Coffee, IceDecorator, MilkDecorator, LemonJuice, OrangeJuice
from product import products
import datetime
import json
from zhipuai import ZhipuAI

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/')
def index():
    # 按类别分组
    categories = {}
    for p in products:
        categories.setdefault(p.category, []).append(p)
    # 智能推荐
    recommend = get_recommendations(session, products)
    # 健康推荐
    health_products = [p for p in products if '低糖' in p.tags or '低脂' in p.tags]
    # 这里补充 category_icons
    category_icons = {
        "碳酸饮料": "fa-bottle-water",
        "矿泉水": "fa-tint",
        "茶饮": "fa-mug-hot",
        "咖啡": "fa-coffee",
        "功能饮料": "fa-bolt",
        "巧克力": "fa-candy-cane",
        "薯片": "fa-cookie",
        "饼干": "fa-cookie-bite",
        "坚果": "fa-seedling",
        "糖果": "fa-candy-cane",
        "糕点": "fa-birthday-cake",
        "饭团": "fa-bowl-rice",
        "三明治": "fa-bread-slice",
        "泡面": "fa-bowl-food",
        "冰淇淋": "fa-ice-cream",
        "冰沙": "fa-glass-martini-alt",
        "个人护理": "fa-first-aid",
        "电子配件": "fa-charging-station",
        "文具": "fa-pen",
        "盲盒": "fa-gift",
        "奇葩口味": "fa-question",
        "本地特产": "fa-map-marker-alt",
        "健康专柜": "fa-heartbeat"
    }
    return render_template(
        'index.html',
        categories=categories,
        recommend=recommend,
        health_products=health_products,
        category_icons=category_icons,
        product_map_json=json.dumps({p.code: {
            "name": p.name,
            "price": p.price,
            "category": p.category
        } for p in products}, ensure_ascii=False)
    )


@app.route('/order', methods=['POST'])
def order():
    beverages = request.form.getlist('beverages')
    if beverages:
        from product import products
        code_map = {p.code: p for p in products}
        orders = []
        total = 0
        for item in beverages:
            # 支持 code|配料:数量
            if ':' in item:
                code_part, qty = item.rsplit(':', 1)
                qty = int(qty)
                if '|' in code_part:
                    code, detail = code_part.split('|', 1)
                else:
                    code, detail = code_part, ''
                product = code_map.get(code)
                if not product:
                    continue
                # 计算加价
                extra = 0
                desc = product.getDescription()
                # 现做饮品配料处理
                if detail:
                    detail_list = detail.split('_')
                    # 这里同步前端的配料加价逻辑
                    for d in detail_list:
                        if d in ['加冰', '冰块']:
                            extra += 1
                        if d in ['奶油']:
                            extra += 2
                    # 拼接配料到描述
                    desc += f'（{"，".join(detail_list)}）'
                unit_cost = product.getPrice() + extra
                order_info = {
                    'description': desc,
                    'unit_cost': unit_cost,
                    'quantity': qty,
                    'total_cost': unit_cost * qty
                }
                orders.append(order_info)
                total += order_info['total_cost']
        if 'orders' not in session:
            session['orders'] = []
        session['orders'].extend(orders)
        session.modified = True
        session['current_order'] = {'orders': orders, 'total': total}
        return render_template('result.html', orders=orders, total=total)
    # 单个饮料下单（原有逻辑）
    beverage_type = request.form.get('beverage')
    ice = request.form.get('ice')
    milk = request.form.get('milk')
    quantity = int(request.form.get('quantity', 1))

    print("beverage_type:", beverage_type)

    if beverage_type == 'coca':
        beverage = Coca()
    elif beverage_type == 'coffee':
        beverage = Coffee()
    elif beverage_type == 'lemonjuice':
        beverage = LemonJuice()
    elif beverage_type == 'orangejuice':
        beverage = OrangeJuice()
    else:
        return render_template('error.html', message="请选择饮料！")

    if ice == 'yes':
        beverage = IceDecorator(beverage)
    if milk == 'yes':
        beverage = MilkDecorator(beverage)

    total_cost = beverage.getCost() * quantity

    order_info = {
        'description': beverage.getDescription(),
        'unit_cost': beverage.getCost(),
        'quantity': quantity,
        'total_cost': total_cost
    }
    if 'orders' not in session:
        session['orders'] = []
    session['orders'].append(order_info)
    session.modified = True
    session['current_order'] = {
        'orders': [order_info],
        'total': total_cost
    }

    return render_template('result.html', orders=[order_info], total=total_cost)


@app.route('/history')
def history():
    orders = session.get('orders', [])
    return render_template('history.html', orders=orders)


@app.route('/pay', methods=['GET', 'POST'])
def pay():
    if request.method == 'POST':
        # 模拟支付成功，清空本次订单（可选）
        session['current_order'] = None
        return render_template('pay_success.html')
    # 获取当前订单金额
    order = session.get('current_order')
    if not order:
        return render_template('error.html', message="没有待支付订单！")
    total = order.get('total', 0)
    return render_template('pay.html', total=total)


def get_recommendations(session, products):
    # 1. 历史推荐
    history = session.get('orders', [])
    history_codes = [order['description'] for order in history[-3:]]  # 最近3单
    history_recommend = [p for p in products if p.name in history_codes]

    # 2. 时段推荐
    hour = datetime.datetime.now().hour
    if 6 <= hour < 11:
        time_recommend = [p for p in products if p.category in ['咖啡', '乳制品']]
    elif 11 <= hour < 14:
        time_recommend = [p for p in products if p.category in ['速食简餐', '健康食品']]
    elif 14 <= hour < 18:
        time_recommend = [p for p in products if p.category in ['零食点心', '茶饮']]
    else:
        time_recommend = [p for p in products if p.category in ['碳酸饮料', '冰品']]

    # 3. 健康推荐
    health_recommend = [p for p in products if '低糖' in p.tags or '低脂' in p.tags]

    # 合并去重
    recommend = []
    for plist in [history_recommend, time_recommend, health_recommend]:
        for p in plist:
            if p not in recommend:
                recommend.append(p)
    return recommend[:6]  # 推荐6个


@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    messages = data.get('messages', [])
    client = ZhipuAI(api_key="91f6e09c4bdc5563f1df70ddc1f10e4f.DF5FnUTxpqab14MS")
    try:
        response = client.chat.completions.create(
            model="glm-4-plus",
            messages=messages
        )
        # 假设 response.choices[0].message.content 是回复内容
        reply = response.choices[0].message.content
        return jsonify({'reply': reply})
    except Exception as e:
        return jsonify({'reply': f'客服暂时不可用：{str(e)}'}), 500


if __name__ == '__main__':
    app.run()
