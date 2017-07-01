package transportationinstall.api

class TiDesignateOrder {
    String id
    String submissionid
    String ordernum
    String partnerid
    String createtime
    Integer status
    String accepttime
    String rejecttime
    String rejectreason
    Integer count
    String remark
    Integer state
    Integer settlementstatus
    Double predictmoney
    Integer version
    Integer auditstatus
//    static hasMany = [tiWorkerDesignateHistory:TiWorkerDesignateHistory]
    static constraints = {
    }
}