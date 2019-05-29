# -*- coding: utf-8 -*-
from libs.BaseWork import LoginBaseClass

class PrepayClass(LoginBaseClass):
    def prepayApi(self,check_ol_bl_pay='on',money=20000,pingzheng='',payment=4,memo='',bank_id=''):
        url = '/member.php?ctl=uc_money&act=incharge_done'
        data = dict(
            check_ol_bl_pay=check_ol_bl_pay,
            money = money ,
            pingzheng = pingzheng,
            payment = payment ,
            memo = memo,
            bank_id = bank_id
        )
        result = self.post_data(url=url,data=data,cookies=self.leibianliang)
        return result