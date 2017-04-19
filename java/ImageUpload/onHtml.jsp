<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8" %>
<%@ include file="/content/myTags.jsp" %>
<%@ include file="/content/myIncludes.jsp" %>
<!DOCTYPE HTML>
<html>
<head>
    <meta charset="utf-8">
    <meta name="renderer" content="webkit|ie-comp|ie-stand">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport"
          content="width=device-width,initial-scale=1,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no"/>
    <meta http-equiv="Cache-Control" content="no-siteapp"/>
    <title>新增婚纱</title>

    <link rel="stylesheet" type="text/css" href="../../../css/ssi-uploader/ssi-uploader.css"/>
    <link rel="stylesheet" type="text/css" href="../../../css/ssi-uploader/bootstrap.min.css"/>
</head>
<body>
<nav class="breadcrumb">
    <i class="Hui-iconfont">&#xe67f;</i> 首页 <span class="c-gray en">&gt;</span>
    婚纱管理 <span class="c-gray en">&gt;</span> 添加婚纱<a
        class="btn btn-success radius r"
        style="line-height: 1.6em; margin-top: 3px"
        href="javascript:location.replace(location.href);" title="刷新"><i
        class="Hui-iconfont">&#xe68f;</i></a>
</nav>
<div class="page-container">
    <div class="col-md-12">
        <h3>添加图片：</h3>
        <input type="file" multiple id="ssi-upload3"/>
    </div>
</div>

<script type="text/javascript" src="../../../css/ssi-uploader/ssi-uploader.js"></script>
<script type="text/javascript" src="../../../css/ssi-uploader/bootstrap.min.js"></script>
<script type="text/javascript">
    $('#ssi-upload3').ssi_uploader({
        url: 'weddingDressCtr/savePicture.do',
        dropZone: false,
        allowed: ['jpg', 'gif', 'txt', 'png', 'pdf']
    });
</script>
</body>
</html>