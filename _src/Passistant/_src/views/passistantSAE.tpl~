<!DOCTYPE html>
<html>
  <head>

    <title>Passistant</title>
    <meta charset="UTF-8">
    <style>
    h1 {
      color: #2F4F4F;
      font-family: courier;
      font-size: 280%;
      text-align: center;
    }
    h3 {
      color:white;
      font-family: courier;
      text-align: center;
    }
    div {
      color: #F92672;
      font-family: courier;
      font-size: 120%;
    }
    div.readlog {
      color: #1E90FF;
      font-family: courier;
      text-align: center;
    }
    i.etime {color: #A6E22E; font-size: 100%}
    i.tags {color: #A6E22E; font-size: 100%}
    pre.diary {color:#E6DB74; font-size: 120%}
    </style>

  </head>
  
  <body style="background-color:black">
    <h1>Passistant／Ｐ助手</h1>
    <h3>Believe me, will help to remember some important things<br>
      like password.<br>
      Begin:</h3>
    <form action="/" method="post">

    <div align="center">
    吐槽: <input type="text" name="newdiary" size="30"/><br>
    标签: <input type="text" name="tags" size="30"/><br> 
    <input value="Submit" type="submit"/>
    </div>
    </form><br>
    %import time
    %for i in diarylog:
      <div class=readlog>
        <i class=etime>{{i['time']}}</i>
        <i class=tags>TAG:{{" ".join(i['tags'])}}</i>
        <pre class=diary>{{i['diary']}}</pre>
      </div>
    %end
  </body>
</html>
