# VEM
一个智能售货机系统

## 安装与运行

1. 安装依赖

   ```bash
   pip install flask zhipuai
   ```

2. 启动服务

   ```bash
   python app.py
   ```

3. 浏览器访问

   ```
   http://127.0.0.1:5000/
   ```

## 常见问题

- **无法访问 GitHub？**  
  请使用科学上网工具（如 Clash、V2RayN）并配置好代理。

- **如何添加商品？**  
  直接在 `product.py` 的 `products` 列表中添加即可。

- **AI客服不可用？**  
  检查 `app.py` 中的 API Key 是否有效，或网络是否畅通。

## 许可证

本项目仅供学习与交流，禁止用于商业用途。
