<div class="m-shop" id="order_${result[0].id}">
    <div class="m-accept"><b>${result[0].ordernum}</b>
        <span>
            <#if result.status gt 3>
                已完成
                <#else>
                    未完成
            </#if>
        </span>
    </div>
    <div class="m-vote"></div>
    <div class="m-vote"><b>计划安装时间：1</b>
        <!--<div class="m-cost">费用预计：<span>￥300</span></div>--></div>
    <div class="m-vote"><b>预约安装时间：</b></div>
    <div class="m-vote"><b>客户姓名：</b></div>
    <div class="m-vote"><b>客户地址：</b></div>
    <div class="m-vote">
        监理姓名：<span></span>
    </div>
    <div class="m-vote">
        监理电话：<span></span>
    </div>
    <div class="m-vote">
        工长姓名：<span></span>
    </div>
    <div class="m-vote">
        工长电话：<span> </span>
    </div>
    <div class="m-vote">
        设计师姓名：<span></span>
    </div>
    <div class="m-vote">
        设计师电话：<span></span>
    </div>
    <div class="m-Line"></div>
    <div class="m-minute">
        <div class="m-info">
            提报记录：
        </div>
        <div id="${result[0].id}"></div>
        <div class="m-Line"></div>
    </div>
    <div class="m-on">
        <input type="hidden" value="${result[0].id}">
        <span>展开</span>
    </div>
</div>