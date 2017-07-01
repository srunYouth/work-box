package transportationinstall.api

import grails.converters.JSON

class TestController {

    def index(){
        try {
//            def user = new Test();
////            user.username = Math.random().toString()
////            user.password = Math.random().toString()
////            user.sex = "NAN"
////            user.save()
////            def users = Test.findAll()
//            def userName = "hfghgj"
//            def users = Test.findAll("from User where username = '${userName}'")[0]
//            users.username = "张三"
//            users.save(flush:true)
//            println(Test.findById(users.id).username)
//            for(u in users){
//                System.err.println(u.username)
//            }
//            System.err.println("action-----------------")
//            def json = request.getSession().getAttribute("id")
//            System.err.println(json)
            System.err.println("=========================")
            for(i in TiWorker.get(1)){
                System.err.println(i.name)
            }

            render("ok")
        }catch (Exception e){
            System.err.println("eroor===========${e}")
            render(e)
        }
    }
    def index2() { }
}
