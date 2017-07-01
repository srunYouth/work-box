package transportationinstall.api

class Test {
    String username
    String password
    static constraints = {
        username blank: true
        password blank: false
    }
}
//// 一对多
//class Author {
//    static hasMany = [ books : Book ]
//    String name
//}
//class Book {
//    String title
//}
//
//// 一对一
//class Face {
//    Nose nose
//}
//class Nose {
//    static belongsTo = [face:Face]
//}
//
//// 多对多
//class Book {
//    static belongsTo = Author
//    static hasMany = [authors:Author]
//    String title
//}
//class Author {
//    static hasMany = [books:Book]
//    String name
//}
