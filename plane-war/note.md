  # 事件监听，代码比较固定！
    
        # 监听事件  
        for event in pygame.event.get():
            # 判断事件类型是否是退出事件
            if event.type == pygame.QUIT:
                print("游戏退出")
                pygame.quit()
                exit()
  # 精灵组
  |pyname.sprite.Sprite|
  |:------------------:|
  |image|
  |rect|
  |:------------------:|
  |update(*args)|
  |kill()|
  |:------------------:|
 
  
  |pygame.sprite.Group|
  |:------------------:|
  |__init__(self,*精灵)|
  |add(*sprites)|
  |sprites()返回所有精灵列表|
  |update(*args)让组中让有精灵调用update方法|
  |draw(Surface)将组中所有精灵的image 绘制到Surface
  的rect位置|
  |:------------------:|
 
 
 * 继承父类，重新初始化方法一定要super()一下父类的__init__方法
 * image有一个get_rect()方法
 
 * 将对象的职责封装在代码内部
 * 尽量简化调用一方的参数
 
 * pygame.time.set_timer(eventid时间代号, milliseconds触发时间)来添加定时器：每隔一段时间执行一些动作
 
        定义 定时器常量——eventid
        
 * 导入模块顺序：官方、第三方、应用程序模块
  
 * if event.type == pygame.KEYDOWN and pygame.K_RIGHT:

 * 
 * event.type == pygame.QUIT:
  
 * event.type == pygame.USEREVENT:（第一个参数事件代号需要基于常量pygame.USEREVENT来指定
USEREVENT是一个整数，在发生事件的事件可以用USEREVENT+1来指定，以此类推）

* pygame中定时器使用套路
1. 创建事件发生的常量  （常量由pygame.USEREVENT来指定）
2. 在初始化方法中调用set_timer()来创建定时器事件
3. 在游戏中监听定时器事件，并作出相应反应。
 
* pygame.key.get_pressed()
* pygame.key.get_pressed()返回所有按键元组
* groupcollide(group1, group2, dokill1（Ture销毁）, dokill2, collided=none)->Sprite_dict
* spritecollide(sprite, group, dokill(精灵组中的对象)，collide=none)->Sprite_list返回所有碰撞的精灵组中的精灵