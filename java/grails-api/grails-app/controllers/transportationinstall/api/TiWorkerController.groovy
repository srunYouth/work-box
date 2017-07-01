package transportationinstall.api

import grails.converters.JSON

class TiWorkerController {

    def index() {
//        def attribute = request.getParameter("workerId")
//        System.err.println(attribute)
//        // 安装工指派单
//        def tiworkerdesignatehistory = TiWorkerDesignateHistory.findByWorkerid("ff8080815c9b7828015c9b891a8700f4")
//        // 提报记录
//        def tiinstalledprogresssubmissionhistory = TiInstalledProgressSubmissionHistory.findAllByDesignateid(tiworkerdesignatehistory.id)
//        def tisubmissionorder = TiSubmissionOrder.findById(TiDesignateOrder.findById(tiworkerdesignatehistory.designateorderid).submissionid)
//        // 客户信息
//        def ticustomer = TiCustomer.findById(tisubmissionorder.customerid)
//        def address = ticustomer.address.split("/")
//        StringBuffer buffer = new StringBuffer()
//        for (int i = 0; i < address.length - 1; i++){
//            def city = SysCitys.findById(address[i].toString()).name
//            buffer.append(city)
//        }
//        buffer.append(address[address.length - 1])
//        ticustomer.setAddress(buffer.toString())
//        for (i in tiinstalledprogresssubmissionhistory){
//            i.l2serid = TiProductSeries.findById(i.l2serid).name
//            i.flowpath = TiInstalledFlowPath.findById(i.flowpath).stepremark
//        }
//        def result = [tiworkerdesignatehistory, ticustomer, tiinstalledprogresssubmissionhistory]
//        def res = tiworkerdesignatehistory as JSON
//        render("callback(" + res +  ")")
//        render(res)
//        def list = TiWorker.list()
//        render(list as JSON)
    }

    def list(){
        def parm = params
        println parm
        TiWorker tiWorker = new TiWorker()
        bindData(tiWorker,parm)
//        println "action -------list"
        def list = TiWorker.findAll(tiWorker)
//        def list = TiWorker.list()
        render(list as JSON)
    }
    def save(){
        try{
            def parm = params
            TiWorker tiWorker = new TiWorker()
            bindData(tiWorker,parm)
//            tiWorker.save(flush:true);
            render("新增成功!")
        }catch (Exception ex){
            System.err.println("错误: ${ex}")
            render("新增失败!")
        }
    }

//    def test(){
//        List list = new ArrayList()
//        list.add(1)
//        list.add(2)
//        list.add(3)
//        list.forEach(e -> {
//            println e
//        })
//    }
}