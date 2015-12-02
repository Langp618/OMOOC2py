%include header title='add|dele'

<h1>= 个人日志系统(Bottle版) =</h1>

<div style="display:none">{{debug}}</div>

<h2>== 日志输入 ==</h2>
<form action="/add" method="POST">
<input type="text" name="txtadd" size="100" maxlength="280"/>
<button type="submit">保存</button>
</form>

<h2>== 历史日志 ==</h2>
<ul>
% for item in HistoryDiary.
  <li>{{item}}
  <sub></sub>
  <sup><a href="/dele/{{item}}">删除</a></sup>
  </li>
%end
</ul>
