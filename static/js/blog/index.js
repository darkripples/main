// blog  index

// 删除记录
function del_blog(id){
    if(confirm("Really DELETE?")){
        $.ajax({
            data : {id:id},
            type : "POST",
            url : "/blog/del_blog/",
            cache : false,
            dataType : "json",
            success: function(data) {
                if(data.flag=="succ"){
                    alert("成功");
                    window.location.reload();
                }else{
                    alert("失败");
                }
            },
            error:function(){
                alert("异常");
            }
        });
    }
    
}