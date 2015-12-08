# Notes for wechat
**s notes for wechat learning**

##服务器配置 - 在SAE上建立服务器.
        设置好二级应用名称, 应用描述等等.

    本地新建关于Mydaily-wechat的一个文件夹. 为了方便管理, 我们统一在Project下建立各种项目的文件夹.

        mkdir Project
        mkdir mydaily-wechat

    初始化仓库, 并与sae建立好的应用相连接.

        $ git init
        $ git remote add sae https://git.sinacloud.com/`App_Name`

         - 注意是二级应用名称.可以在应用设置里看到.
         - `sae`可以替换成你任务不容易欢笑的名称, 比如我就改成了`mwechat`.

1. 当普通微信用户向公众账号发消息时，微信服务器将POST消息的XML数据包到开发者填写的URL上
 <xml>
 <ToUserName><![CDATA[toUser]]></ToUserName>
 <FromUserName><![CDATA[fromUser]]></FromUserName> 
 <CreateTime>1348831860</CreateTime>
 <MsgType><![CDATA[text]]></MsgType>
 <Content><![CDATA[this is a test]]></Content>
 <MsgId>1234567890123456</MsgId>
 </xml>
2. example-> http://www.cnblogs.com/weishun/p/weixin-publish-developing.html