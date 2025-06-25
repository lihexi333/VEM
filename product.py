class Product:
    def __init__(self, code, name, category, price, calories, nutrition, tags=None, description="", available_ingredients=None):
        self.code = code
        self.name = name
        self.category = category
        self.price = price
        self.calories = calories
        self.nutrition = nutrition
        self.tags = tags or []
        self.description = description
        self.available_ingredients = available_ingredients or []

    def getDescription(self):
        return self.name + (f"（{self.description}）" if self.description else "")

    def getPrice(self):
        return self.price

# 饮品示例
products = [
    Product("coca", "可乐", "碳酸饮料", 3.0, 140, "碳水: 35g, 糖: 35g", ["高糖"], "经典可乐", available_ingredients=["冰块", "柠檬", "糖浆"]),
    Product("coca_zero", "零度可乐", "碳酸饮料", 3.5, 0, "碳水: 0g, 糖: 0g", ["低糖", "低热量"], "无糖可乐", available_ingredients=["冰块", "柠檬", "糖浆"]),
    Product("sprite", "雪碧", "碳酸饮料", 3.0, 140, "碳水: 36g, 糖: 36g", ["高糖"], "清爽雪碧", available_ingredients=["冰块", "柠檬", "糖浆"]),
    Product("fanta", "芬达", "碳酸饮料", 3.0, 150, "碳水: 38g, 糖: 38g", ["高糖"], "橙味芬达", available_ingredients=["冰块", "柠檬", "糖浆"]),
    Product("evian", "依云矿泉水", "矿泉水", 6.0, 0, "无", ["进口"], "高端进口矿泉水"),
    Product("oolong_tea", "乌龙茶", "茶饮", 4.0, 0, "碳水: 0g, 糖: 0g", ["无糖"], "清香乌龙茶", available_ingredients=["冰块", "柠檬", "珍珠"]),
    Product("redbull", "红牛", "功能饮料", 6.0, 110, "碳水: 27g, 糖: 27g", ["提神型"], "能量补充", available_ingredients=["冰块", "柠檬"]),
    Product("snickers", "士力架", "巧克力", 4.5, 250, "蛋白质: 4g, 碳水: 33g, 脂肪: 12g", ["白巧草莓"], "能量巧克力棒"),
    Product("chips", "原味薯片", "薯片", 4.0, 200, "碳水: 20g, 脂肪: 10g", ["厚切"], "香脆薯片"),
    Product("oreo", "奥利奥", "饼干", 3.5, 120, "蛋白质: 1g, 碳水: 20g, 脂肪: 5g", ["低糖"], "经典夹心饼干"),
    Product("pistachio", "开心果", "坚果", 8.0, 160, "蛋白质: 6g, 碳水: 8g, 脂肪: 13g", ["蜂蜜烘焙"], "健康坚果"),
    Product("mint_candy", "薄荷糖", "糖果", 2.0, 60, "碳水: 15g, 糖: 15g", ["大白兔"], "清新口气"),
    Product("muffin", "玛芬蛋糕", "糕点", 5.0, 220, "蛋白质: 3g, 碳水: 30g, 脂肪: 10g", ["无麸质"], "松软蛋糕"),
    Product("tuna_riceball", "金枪鱼饭团", "饭团", 7.0, 180, "蛋白质: 6g, 碳水: 32g, 脂肪: 3g", ["日式三角"], "日式便携饭团"),
    Product("egg_sandwich", "鸡蛋沙拉三明治", "三明治", 8.0, 210, "蛋白质: 8g, 碳水: 28g, 脂肪: 7g", ["冷藏"], "营养早餐"),
    Product("beef_noodle", "红烧牛肉泡面", "泡面", 6.0, 350, "蛋白质: 8g, 碳水: 55g, 脂肪: 12g", ["自热锅"], "方便速食"),
    Product("ice_cream", "甜筒冰淇淋", "冰淇淋", 5.0, 200, "蛋白质: 3g, 碳水: 25g, 脂肪: 10g", ["奥利奥联名"], "夏日冰爽"),
    Product("mango_smoothie", "芒果冰沙", "冰沙", 6.0, 160, "蛋白质: 1g, 碳水: 38g, 脂肪: 0g", ["加珍珠"], "清凉解暑"),
    Product("mask", "口罩", "个人护理", 2.0, 0, "无", ["便携装"], "健康防护"),
    Product("cable", "充电线", "电子配件", 10.0, 0, "无", ["通用接口"], "多功能充电线"),
    Product("note", "便签纸", "文具", 3.0, 0, "无", ["迷你尺寸"], "办公学习必备"),
    Product("snack_box", "零食盲盒", "盲盒", 15.0, 300, "蛋白质: 5g, 碳水: 50g, 脂肪: 10g", ["限量隐藏款"], "惊喜组合"),
    Product("cilantro_chips", "香菜味薯片", "奇葩口味", 4.0, 200, "碳水: 20g, 脂肪: 10g", ["社交话题"], "奇特口味"),
    Product("chengdu_biscuit", "成都辣酱饼干", "本地特产", 8.0, 180, "蛋白质: 3g, 碳水: 30g, 脂肪: 6g", ["旅游打卡"], "地方特色"),
    Product("protein_powder", "蛋白粉小包", "健康专柜", 12.0, 100, "蛋白质: 20g, 碳水: 5g, 脂肪: 1g", ["高蛋白"], "健身补剂"),
    Product("milk_tea", "奶茶", "现做饮品", 8.0, 220, "蛋白质: 4g, 碳水: 32g, 脂肪: 8g", ["现做"], "香浓奶茶", available_ingredients=["全糖", "七分糖", "五分糖", "无糖", "冰块"]),
    Product("fresh_coffee", "咖啡", "现做饮品", 10.0, 80, "蛋白质: 2g, 碳水: 5g, 脂肪: 3g", ["现做"], "手冲咖啡", available_ingredients=["奶油", "冰块"]),
    Product("yibao", "怡宝矿泉水", "矿泉水", 2.0, 0, "无", ["国产"], "清爽怡宝"),
    Product("baishui", "百岁山矿泉水", "矿泉水", 4.0, 0, "无", ["高端"], "天然矿泉"),
    Product("nongfu", "农夫山泉", "矿泉水", 3.0, 0, "无", ["天然"], "有点甜"),
    Product("scream", "尖叫", "功能饮料", 4.0, 80, "碳水: 20g, 糖: 20g", ["运动型"], "补充能量"),
    Product("lehu", "乐虎", "功能饮料", 5.0, 90, "碳水: 22g, 糖: 22g", ["提神"], "维生素饮料"),
    Product("mozhua", "魔爪", "功能饮料", 3.0, 100, "碳水: 25g, 糖: 25g", ["能量"], "能量饮料"),
    Product("dove", "德芙", "巧克力", 4.0, 210, "蛋白质: 2g, 碳水: 24g, 脂肪: 13g", ["丝滑"], "经典巧克力"),
    Product("mailisu", "麦丽素", "巧克力", 2.0, 120, "蛋白质: 1g, 碳水: 15g, 脂肪: 6g", ["麦芽"], "麦芽脆心"),
    Product("cuicuisha", "脆脆鲨", "巧克力", 2.0, 130, "蛋白质: 1g, 碳水: 16g, 脂肪: 7g", ["威化"], "威化巧克力棒"),
    Product("lays", "乐事薯片", "薯片", 4.0, 210, "碳水: 22g, 脂肪: 11g", ["原味"], "经典乐事"),
    Product("pringles", "品客薯片", "薯片", 5.0, 220, "碳水: 23g, 脂肪: 12g", ["进口"], "原装进口"),
    Product("kaixinguo", "开小灶薯片", "薯片", 3.0, 180, "碳水: 18g, 脂肪: 9g", ["薄片"], "轻薄口感"),
    Product("vitamin_c", "维生素C咀嚼片", "健康专柜", 6.0, 30, "维生素C: 100mg", ["补充维C"], "每日健康"),
    Product("lowfat_milk", "低脂牛奶", "健康专柜", 5.0, 80, "蛋白质: 5g, 碳水: 9g, 脂肪: 2g", ["低脂"], "健康饮品"),
    Product("energy_bar", "能量棒", "健康专柜", 7.0, 120, "蛋白质: 8g, 碳水: 15g, 脂肪: 3g", ["高蛋白"], "健身补给"),
    Product("gel_pen", "中性笔", "文具", 2.0, 0, "无", ["书写"], "顺滑书写"),
    Product("eraser", "橡皮擦", "文具", 1.0, 0, "无", ["学习"], "干净擦除"),
    Product("notebook", "笔记本", "文具", 5.0, 0, "无", ["记事"], "学习办公"),
    Product("usb_drive", "U盘16G", "电子配件", 18.0, 0, "无", ["存储"], "高速U盘"),
    Product("mouse", "无线鼠标", "电子配件", 25.0, 0, "无", ["便携"], "办公必备"),
    Product("earphone", "有线耳机", "电子配件", 12.0, 0, "无", ["音乐"], "清晰音质"),
    Product("uni_noodle", "统一老坛酸菜牛肉面", "泡面", 5.0, 350, "蛋白质: 7g, 碳水: 54g, 脂肪: 13g", ["酸菜"], "经典口味"),
    Product("jinfeng", "今麦郎拉面", "泡面", 4.0, 320, "蛋白质: 6g, 碳水: 50g, 脂肪: 11g", ["劲道"], "劲道拉面"),
    Product("kangshifu", "康师傅红烧排骨面", "泡面", 5.0, 340, "蛋白质: 8g, 碳水: 53g, 脂肪: 12g", ["红烧"], "家常美味"),
    Product("ham_sandwich", "火腿三明治", "三明治", 7.0, 220, "蛋白质: 9g, 碳水: 28g, 脂肪: 8g", ["早餐"], "营养美味"),
    Product("tuna_sandwich", "金枪鱼三明治", "三明治", 8.0, 210, "蛋白质: 10g, 碳水: 27g, 脂肪: 7g", ["健康"], "低脂高蛋白"),
    Product("vege_sandwich", "蔬菜三明治", "三明治", 6.0, 180, "蛋白质: 5g, 碳水: 25g, 脂肪: 5g", ["素食"], "清新健康"),
    Product("salmon_riceball", "三文鱼饭团", "饭团", 7.0, 170, "蛋白质: 7g, 碳水: 30g, 脂肪: 3g", ["日式"], "三文鱼夹心"),
    Product("plum_riceball", "梅子饭团", "饭团", 6.0, 160, "蛋白质: 4g, 碳水: 28g, 脂肪: 2g", ["酸甜"], "梅子风味"),
    Product("beef_riceball", "牛肉饭团", "饭团", 8.0, 190, "蛋白质: 8g, 碳水: 32g, 脂肪: 4g", ["肉类"], "牛肉夹心"),
    Product("egg_tart", "蛋挞", "糕点", 4.0, 180, "蛋白质: 3g, 碳水: 20g, 脂肪: 9g", ["甜品"], "酥皮蛋挞"),
    Product("cheese_cake", "芝士蛋糕", "糕点", 6.0, 250, "蛋白质: 5g, 碳水: 28g, 脂肪: 14g", ["芝士"], "浓郁芝士"),
    Product("swiss_roll", "瑞士卷", "糕点", 5.0, 200, "蛋白质: 4g, 碳水: 26g, 脂肪: 8g", ["蛋糕"], "松软可口"),
    Product("fruit_candy", "水果糖", "糖果", 2.0, 70, "碳水: 18g, 糖: 18g", ["水果"], "多种口味"),
    Product("cola_candy", "可乐糖", "糖果", 2.0, 65, "碳水: 16g, 糖: 16g", ["可乐味"], "可乐风味"),
    Product("gummy_bear", "小熊软糖", "糖果", 3.0, 80, "碳水: 20g, 糖: 20g", ["软糖"], "Q弹美味"),
    Product("almond", "扁桃仁", "坚果", 7.0, 170, "蛋白质: 6g, 碳水: 7g, 脂肪: 15g", ["高纤"], "健康坚果"),
    Product("cashew", "腰果", "坚果", 8.0, 180, "蛋白质: 5g, 碳水: 9g, 脂肪: 14g", ["营养"], "香脆腰果"),
    Product("walnut", "核桃仁", "坚果", 9.0, 190, "蛋白质: 4g, 碳水: 8g, 脂肪: 18g", ["补脑"], "优质核桃"),
    Product("digestive", "消化饼干", "饼干", 3.0, 110, "蛋白质: 2g, 碳水: 18g, 脂肪: 4g", ["高纤"], "健康消化"),
    Product("lemon_biscuit", "柠檬饼干", "饼干", 3.5, 115, "蛋白质: 1g, 碳水: 19g, 脂肪: 4g", ["清新"], "柠檬风味"),
    Product("butter_cookie", "黄油曲奇", "饼干", 4.0, 130, "蛋白质: 2g, 碳水: 16g, 脂肪: 6g", ["曲奇"], "香浓黄油"),
]

for p in products:
    if p.category in ["茶饮", "咖啡"]:
        p.category = "现做饮品"
        if p.code == "oolong_tea":
            p.available_ingredients = ["冰块", "柠檬", "珍珠"]
        elif p.code == "milk_tea":
            p.available_ingredients = ["全糖", "七分糖", "五分糖", "无糖", "冰块"]
        elif p.code == "fresh_coffee":
            p.available_ingredients = ["奶油", "冰块"]
