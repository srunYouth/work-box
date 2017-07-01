package transportationinstall.api

class TiPartnerContract {
    String id
    String contractnum
    String resourcepartnerid
    String installpartnerid
    String cityid
    String contactpeoplename
    String contactphonenumber
    String companyaddress
    String legalperson
    String starttime
    String endtime
    Integer status
    Double secondaryrepairfee
    Double firstdelaydeductmoney
    Double seconddelaydeductmoney
    Double validityduration
    Integer version
    String contractattachment
    static constraints = {
    }
}