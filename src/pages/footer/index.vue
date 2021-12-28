<template>
  <div id="footer">
    <div class="ft-bg">
      <div class="w-ensure mb20">
        <div class="w-main">
          <ul>
            <li>
              <a>
                <img
                  width="300"
                  height="90"
                  src="../../assets/ft-svr1.gif"
                  alt="底部导航图片"
                />
              </a>
            </li>
            <li>
              <a
                ><img
                  width="300"
                  height="90"
                  src="../../assets/ft-svr2.gif"
                  alt="底部导航图片"
                />
              </a>
            </li>
            <li>
              <a
                ><img
                  width="300"
                  height="90"
                  src="../../assets/ft-svr3.gif"
                  alt="底部导航图片"
                />
              </a>
            </li>
            <li>
              <a>
                <img
                  width="300"
                  height="90"
                  src="../../assets/ft-svr4.gif"
                  alt="底部导航图片"
                />
              </a>
            </li>
          </ul>
        </div>
        <div class="ft_main"></div>
        <div class="ft_txt">
          <p class="ft_contact">
            <span>服务时间：09:00-23:00</span>
            <span class="ft_phone">客服热线: <em>010-88888888</em></span>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {};
</script>

<style scoped  lang='scss'>
html {
  background: #fafafa;
  color: #333;
  _background-attachment: fixed;
}

body,
p,
ul,
li {
  margin: 0;
  padding: 0;
}
body {
  font: 12px/1.5 "Microsoft YaHei", Tahoma, Helvetica, Arial, simsun;
}
i {
  font-style: normal;
}
ul {
  list-style: none;
}
img {
  border: 0;
}
a {
  text-decoration: none;
  color: #333;
  -webkit-transition: color 0.2s;
  -moz-transition: color 0.2s;
  -o-transition: color 0.2s;
  -ms-transition: color 0.2s;
  transition: color 0.2s;
}
a:hover {
  color: #09c762;
}
a:focus,
area:focus {
  outline: 0;
}
// 底部样式编写
#footer {
  border-top: 1px solid #eee;
  background: #fff;
}
#footer .ft_main {
  width: 1196px;
  margin: 0 auto;
}
#footer .w-main {
  margin: 0 auto;
  width: 1200px;
}
#footer .ft_cata {
  display: none;
}
#footer .w-ensure {
  background: #09c762 none repeat scroll 0 0;
  height: 90px;
}
#footer .w-ensure li {
  float: left;
  font-size: 0;
}
/* 清除浮动 */
#footer .w-main::after {
  clear: both;
  content: "";
  display: table;
}
/* 对应字体文本 */
#footer .ft_txt {
  text-align: center;
  padding: 8px 0;
}
#footer .ft_txt p {
  padding: 5px 0;
  color: #666;
}

#footer .ft_txt .ft_phone {
  font-size: 14px;
}

#footer .ft_txt .ft_phone em {
  color: #09c762;
  font-weight: bold;
  font-size: 24px;
}
#footer .ft_txt .ft_contact span {
  display: inline-block;
  padding: 0 20px;
}
</style>