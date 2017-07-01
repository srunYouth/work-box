package transportationinstall.api

class TiInstalledProgressSubmissionHistory {
    String id
    String l2serid
    String productid
    String designateid
    String createtime
    String flowpath
    String remark
    Integer version
    Integer status
    String exceptionid
    Integer sign1
//    static belongsTo = TiDesignateOrder
//    static hasMany = [tiDesignateOrder:TiDesignateOrder]
    static constraints = {
    }
}