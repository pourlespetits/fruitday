$(function(){
    check_login();
    loadGoods();
});


/*  异步验证登录状态
    如果已登录,显示:欢迎uname  退出
    如果未登录,显示:[登录][注册有惊喜]
*/
function check_login(){
    $.get('/check_login/',function(data){
        var html = '';
        var $isActive = $("#list>li:first");
        if (data.lgStatus == 0) {
            html += "<a href='/login/'>[登录]</a> , ";
            html += "<a href='/register/'>[注册有惊喜]</a>"
        }else{
            html += "欢迎:" + data.uname;
            html += "&nbsp;&nbsp;<a href='/quit/'>退出</a>"
        }
        console.log(data);
        $isActive.html(html);
    },'json');
}

// 异步加载商品类型以及商品列表
function loadGoods(){

    $.get('/getSource/', function(data){
        var show = '';
        // console.log('show');
        $.each(data, function(i, obj){
            // console.log(obj);
            var html ="<div class='item'>";
            // 将obj.typeobj转换为jison对象
            typeobj = JSON.parse(obj.typeobj);
            // console.log(typeobj);
            html +="<p class='title'>"
              html +="<a href='#''>更多</a>";
              html +="<img src='/" + typeobj.picture +"'>";
            html +="</p>";
            html +="<ul>";
            // 将obj.goods有字符串转换为json对象
            jsonGoods = JSON.parse(obj.goods);
            // console.log(jsonGoods);
            // 遍历商品
            $.each(jsonGoods, function(i, good){
                // console.log(good.fields);
                if (i == 4 || i==9) {
                    
                    html += "<li class='no-margin'>";
                }else{
                    html += "<li>";
                }
                // 加载li中的内容
                html +="<p>";
                html +="<img src='/"+good.fields.picture+"'>";
                html +="</p>";
                html +="<div class='content'>";
                  html +="<a href='javascript:add_cart("+good.pk+");' class='cart'>\
                            <img src='/static/images/cart.png'>\
                        </a>";
                  html +="<p>"+good.fields.title+"</p>";

                  html +="<span>&yen;";
                  html += good.fields.price+"/"+good.fields.spec;
                  html +="</span>";
                html +="</div>";
                html += "</li>";
            });
            html +="</ul>"

            html +="</div>";
            // console.log(html);
            show += html;
        });
       $('#main').html(show);

    }, 'json');
}


//添加商品到购物车
//参数good_id:需要添加至购物车的商品的id
function add_cart(good_id){
    // 验证用户是否登录,如果未登录,则给出提示

    $.get('/check_login/',function(data){
        if(data.lgStatus == 0){
            alert("请先登录");
        }else{
            // alert("将商品加入至购物车");
            $.post('/add_cart/',{
                'goodid':good_id,
                'csrfmiddlewaretoken': $.cookie('csrftoken')
            },function(data){
                console.log(good_id);
                if (data.status == 1) {
                    alert(data.statusText);
                }else{
                    alert("添加购物车成功");
                }
            },'json');
        }
    },'json');
}


