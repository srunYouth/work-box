//var _json = {
//	"id": "ff8080815c9b7828015c9ba206300151",
//	"accepttime": "2017-06-12 17:27:43.0",
//	"appointmenttime": "2017-06-13 00:00:00.0",
//	"auditstatus": 0,
//	"createtime": "2017-06-12 17:28:26.0",
//	"designateorderid": "ff8080815c9b7828015c9b8a10da0105",
//	"ordernum": "TIWDO17061218604092604953584",
//	"rejectreason": null,
//	"rejecttime": null,
//	"status": 2,
//	"teamid": "2",
//	"workerid": "ff8080815c9b7828015c9b891a8700f4"
//}

var _user = {
	"username": "admin@admin",
	"password": "admin"
}

function toAjax() {
	//	$.ajax({
	//		async: false,
	//		type: 'GET',
	//		url: "json/order.json",
	//		dataType: 'json',
	//		processData: false,
	//		success: function(data) {
	//			d = data
	//		}
	//	})
	//	return d;
	return _user
}

//			function toAjax() {
//				console.log("action")
//				url = "http://localhost:8080/tiWorker/index"
//				$.ajax({
//					async: false,
//					type: 'GET',
//					url: url,
//					dataType: 'jsonp',
//					success: function(data) {
//						console.log("success")
//					},
//					error: function(XMLHttpRequest, textStatus, errorThrown) {
//						console.error("error")
//					}
//				}).complete(function(data) {
//					console.log("complete")
//					d = data;
//				});
//				return d;
//			}

//			function callback(data) {
//				console.log("callback")
//				d = data
//			}

/*var _json = [
	{
		"id": "1",
		"address": "山东省单县徐寨镇韩庄行政村韩庄213号",
		"arbitration": "",
		"checkstatus": 2,
		"contracttime": 1.0,
		"experience": "优秀",
		"headportrait": "",
		"idcard": "372925199106127337",
		"idcardback": "",
		"idcardfront": "",
		"insurance": "",
		"isinsurance": 0,
		"isreconciliation": 1,
		"name": "时世腾",
		"password": "c4ca4238a0b923820dcc509a6f75849b",
		"phonenum": "18844025830",
		"status": 0,
		"teamid": "3"
	}, {
		"id": "2",
		"address": "福建省罗源县飞竹镇丰余村林社11号",
		"arbitration": "",
		"checkstatus": 2,
		"contracttime": 1.0,
		"experience": "优秀",
		"headportrait": "",
		"idcard": "350123197705034553",
		"idcardback": "",
		"idcardfront": "",
		"insurance": "",
		"isinsurance": 0,
		"isreconciliation": 1,
		"name": "林达江",
		"password": "c4ca4238a0b923820dcc509a6f75849b",
		"phonenum": "13459196463",
		"status": 0,
		"teamid": "3"
	}, {
		"id": "3",
		"address": "福建省武平县武东乡黄埔村老屋路17号",
		"arbitration": "",
		"checkstatus": 2,
		"contracttime": 1.0,
		"experience": "优秀",
		"headportrait": "",
		"idcard": "352625197811055472",
		"idcardback": "",
		"idcardfront": "",
		"insurance": "",
		"isinsurance": 0,
		"isreconciliation": 1,
		"name": "林杨",
		"password": "c4ca4238a0b923820dcc509a6f75849b",
		"phonenum": "13063035987",
		"status": 0,
		"teamid": "3"
	}, {
		"id": "4",
		"address": "江苏省丰县王沟镇许庙村董庄131号",
		"arbitration": "",
		"checkstatus": 2,
		"contracttime": 1.0,
		"experience": "优秀",
		"headportrait": "",
		"idcard": "320321199401014416",
		"idcardback": "",
		"idcardfront": "",
		"insurance": "",
		"isinsurance": 0,
		"isreconciliation": 1,
		"name": "董要要",
		"password": "c4ca4238a0b923820dcc509a6f75849b",
		"phonenum": "15262095757",
		"status": 0,
		"teamid": "3"
	}, {
		"id": "5",
		"address": "河北省邯郸市涉县合漳乡断曲村5组30号",
		"arbitration": "",
		"checkstatus": 2,
		"contracttime": 1.0,
		"experience": "优秀",
		"headportrait": "",
		"idcard": "130426197306305015",
		"idcardback": "",
		"idcardfront": "",
		"insurance": "",
		"isinsurance": 0,
		"isreconciliation": 1,
		"name": "刘军生",
		"password": "123",
		"phonenum": "13910076460",
		"status": 0,
		"teamid": "3"
	}, {
		"id": "6",
		"address": "河北省保定市涞水县义安镇北高洛村西上坎",
		"arbitration": "",
		"checkstatus": 2,
		"contracttime": 1.0,
		"experience": "优秀",
		"headportrait": "",
		"idcard": "130623198807301510",
		"idcardback": "",
		"idcardfront": "",
		"insurance": "",
		"isinsurance": 0,
		"isreconciliation": 1,
		"name": "李秀颖",
		"password": "c4ca4238a0b923820dcc509a6f75849b",
		"phonenum": "15128485850",
		"status": 0,
		"teamid": "3"
	}, {
		"id": "7",
		"address": "河南省郸城县钱店镇大庄行政村",
		"arbitration": "",
		"checkstatus": 2,
		"contracttime": 1.0,
		"experience": "优秀",
		"headportrait": "",
		"idcard": "412726198702256219",
		"idcardback": "",
		"idcardfront": "",
		"insurance": "",
		"isinsurance": 0,
		"isreconciliation": 1,
		"name": "崔荣伟",
		"password": "c4ca4238a0b923820dcc509a6f75849b",
		"phonenum": "13699169952",
		"status": 0,
		"teamid": "1"
	}, {
		"id": "9",
		"address": "黑龙江省齐齐哈尔市梅里斯区梅里斯孙散居5组",
		"arbitration": "",
		"checkstatus": 1,
		"contracttime": 1.0,
		"experience": "优秀",
		"headportrait": "",
		"idcard": "230208198409201176",
		"idcardback": "",
		"idcardfront": "",
		"insurance": "",
		"isinsurance": 0,
		"isreconciliation": 0,
		"name": "西震",
		"password": "71b9e42fd1490c2ee83c1bc4c4e37da3",
		"phonenum": "13370170435",
		"status": 0,
		"teamid": "2"
	}, {
		"id": "ff8080815c43df36015c48c4892900ce",
		"address": "北京",
		"arbitration": "",
		"checkstatus": 2,
		"contracttime": null,
		"experience": "12321312",
		"headportrait": "",
		"idcard": "",
		"idcardback": "",
		"idcardfront": "",
		"insurance": "",
		"isinsurance": 0,
		"isreconciliation": 0,
		"name": "高平",
		"password": "c4ca4238a0b923820dcc509a6f75849b",
		"phonenum": "15843534432",
		"status": 0,
		"teamid": "1"
	}, {
		"id": "ff8080815c9b7828015c9b891a8700f4",
		"address": "阿斯达撒大 ",
		"arbitration": "",
		"checkstatus": 2,
		"contracttime": null,
		"experience": "萨达是",
		"headportrait": "",
		"idcard": "",
		"idcardback": "",
		"idcardfront": "",
		"insurance": "",
		"isinsurance": 0,
		"isreconciliation": 1,
		"name": "张张张",
		"password": "e10adc3949ba59abbe56e057f20f883e",
		"phonenum": "13822222222",
		"status": 0,
		"teamid": "2"
	}
]*/