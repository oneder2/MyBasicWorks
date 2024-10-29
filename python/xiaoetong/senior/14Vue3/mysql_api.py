from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import *
# 首先安装好flask模块，flask_cors模块，sqlalchemy模块，和mysql-connector-python模块

# 创建Flask应用实例
app = Flask(__name__)
# 配置CORS跨域资源共享，允许所有来源访问/api/*路径
CORS(app, resources={r"/api/*": {"origins": "*"}})
# 创建引擎对象      root:root@localhost/user_api    root用户名  root密码 user_api是我mysql的一个数据库
engine = create_engine('mysql+mysqlconnector://root:root@localhost/user_api')

# 创建会话类，用于管理数据库会话
Session = sessionmaker(bind=engine)

# 创建基类，用于定义数据模型
Base = declarative_base()
# 如果以上代码运行报错，请注释上面base这行代码，用下面这句
# Base = sqlalchemy.orm.declarative_base()


# 定义数据模型，映射到数据库的items表
class Item(Base):
    # 指定表名
    __tablename__ = 'items'
    # 字段id，name，以及类型和约束
    id = Column(Integer, primary_key=True) # 定义id字段，设置为主键
    name = Column(String(255)) # 定义name字段，类型为字符串


# 获取所有项目
@app.route('/api/items', methods=['GET'])
def get_items():
    session = Session() # 创建会话
    print("连接到 MySQL 数据库")
    items = session.query(Item).all() # 查询所有Item记录
    session.close()
    # 将查询结果转换为JSON格式返回
    return jsonify([{'id': item.id, 'name': item.name} for item in items])


# 添加新项目
# 添加新项目
@app.route('/api/items', methods=['POST'])
def add_item():
    name = request.json['name'] # 从请求中获取name参数
    session = Session()
    print("连接到 MySQL 数据库，正在进行添加操作")
    new_item = Item(name=name)  # 创建新的Item实例
    session.add(new_item)  # 将新实例添加到会话
    session.commit() # 提交事务
    session.refresh(new_item)  # # 刷新新对象，以获取数据库生成的id
    session.close()
    return jsonify({'id': new_item.id, 'name': new_item.name})


# 删除项目
@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    session = Session()
    print("连接到 MySQL 数据库，正在进行删除操作")
    # 根据id获取要删除的项目
    item_to_delete = session.query(Item).get(item_id)
    if item_to_delete: # 如果项目存在
        session.delete(item_to_delete) # 删除项目
        session.commit()
        session.close()
        # 返回204状态码，表示删除成功
        return '', 204
    else:
        # 返回404状态码，表示项目未找到
        return jsonify({'error': 'Item not found'}), 404


# 更新项目
@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    name = request.json['name'] # 从请求中获取name参数
    session = Session()
    print("连接到 MySQL 数据库，正在进行修改操作")
    item_to_update = session.query(Item).get(item_id)
    if item_to_update:
        item_to_update.name = name
        session.commit()
        session.close()
        return '', 204
    else:
        return jsonify({'error': '没有找到元素'}), 404


if __name__ == '__main__':
    app.run(debug=True)
