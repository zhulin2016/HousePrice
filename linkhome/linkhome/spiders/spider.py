# -*- coding: utf-8 -*-

import scrapy
import commands
no = 0
number_global = []
date = commands.getoutput("date +%y-%m-%d_%H")
#date = date[0:12]

#date += "H.txt"
from linkhome.items import LinkhomeItem

class Linkhome_Spider(scrapy.Spider):
    name = "linkhome1"
    allowed_domains = ['http://bj.lianjia.com/ershoufang/']
    start_urls = []
    f = open('link.txt','r')
    for each in f:
        each = each.split("\n")[0]
	print(each)
        start_urls.append(each)
	print(start_urls)
    print(start_urls)
    date2 = date
    date2 += "H.txt"
    try:
        f = open(date2,'r')
        f.close()
    except:
        f = open(date2,'w')
        f.close()
    def parse(self, response):
        date2 = date
	date2 += "H.txt"
	sel = scrapy.selector.Selector(response)
        page = sel.xpath('//div[@class="page-box house-lst-page-box"]').extract()
        for each in page:
            page0 = str(each).split('"totalPage":')[1].split(",")[0]
	    item2 = str(each).split('{page}')[1].split('"')[0]
        page_num = int(page0)
        item1 = "http://bj.lianjia.com/ershoufang/"
        items = item1 +item2
        for i in range(page_num):
            j = i + 2
            if( j <= page_num):
                items += "\n"
                items += item1
		items += "pg"
                items += str(j)
                items += item2
	items += "\n"
        f = open(date2,'a')
        f.write(items)
        f.close()

class Linkhome2_Spider(scrapy.Spider):
    name = "linkhome2"
    allowed_domains = ['http://bj.lianjia.com/ershoufang/']
    start_urls = [] 
    date2 = date
    date2 += "H.txt"
    f = open(date2,'r')
    for each in f:
        each = each.split("\n")[0]
        start_urls.append(each)
    f.close()
       
    def parse(self,response):
        date1 = date
        date1 += "H.json"
        sel = scrapy.selector.Selector(response)   
        sites = sel.xpath('//ul[@class="listContent"]/li/a')
       
	items = "\n"
        for site in sites:
            #房源链接
            items += "\n"
            items += str(site.xpath('@href').extract())
            #items.append(item)
	print(items)	
        f = open(date1,'a')
        f.write(items)
        f.close()


class Linkhome3_Spider(scrapy.Spider):
    name = "linkhome3"
    allowed_domains = ['http://bj.lianjia.com/ershoufang/']
    #start_urls = ['http://bj.lianjia.com/ershoufang/101100214471.html','http://bj.lianjia.com/ershoufang/101092058294.html']
 
    #从前一个蜘蛛爬的结果里导入链接到本蜘蛛的start_urls的列表里。

    start_urls = []
    date3 = date
    date3 += "H.json"
    try:
        f = open(date3,'r')
    except:
        f = open(date3,'w')
        f.close()
 
    f = open(date3,'r')
    for each in f:
	if each != "\n":
		temp = each.split("u'")[-1].split("'")[0]
		start_urls.append(temp)
    print(start_urls)

    '''
    temp3 =''
    for each in f:
        if each != "\n":
            temp = each.split("u'")[-1].split("'")[0]
            temp3 += str(temp)
            temp3 += "\n"
    f = open('spider2.txt','w')
    f.write(temp3)
    #print(temp3)
    f.close()
    f = open('spider2.txt','r')
    for each in f:
        each = each.split("\n")[0]
        start_urls.append(each)
    '''
    #对本蜘蛛要爬取的链接挨个爬取目标内容
    def parse(self, response):
        global no
        items = []
        item = LinkhomeItem()
        sel = scrapy.selector.Selector(response)

        #楼层
        bases = sel.xpath('//div[@class="introContent"]/div[@class="base"]').extract()
        baseinfo = "\n"
        for base in bases:
            baseinfo += base
            baseinfo = baseinfo.encode("GBK")   
        floor = str(baseinfo).split("label")[2].split("span")[1].split("<")[0].split(">")[1]
        floor = floor[0:6]
        floor_remark = floor.decode("GBK")
        
        #年代
        ages = sel.xpath('//div[@class="area"]/div[@class="subInfo"]').extract()
        temp = ""
        for each in ages:
            temp += each.split(">")[1].split("<")[0]
        age = ''
        temp = temp[0:len(temp)]
        for a in temp:
            if(a.isdigit() == True):
                age += a
        age = int(age)

        #价格
        prices = sel.xpath('//span[@class="total"]').extract()
        price = ""
        for each in prices:
            price += each.split(">")[1].split("<")[0]
        unit_price = ""
        prices = sel.xpath('//span[@class="unitPriceValue"]').extract()
        for each in prices:
            unit_price += each.split(">")[1].split("<")[0]        
        price = int(price)

        #满五唯一
        bases2 = sel.xpath('//div[@class="transaction"]/div[@class="content"]').extract()
        base2info = "\n"
        for base in bases2:
            base2info += base
        base2info = base2info.encode("GBK")
        feature = ""
        feature1 = base2info.split("label")[5].split("span")[1].split("<")[0].split(">")[1]     #满五
        feature2 = base2info.split("label")[7].split("span")[1].split("<")[0].split(">")[1]    #唯一
        feature3 = base2info.split("label")[8].split("span")[1].split("<")[0].split(">")[1]    #经适房/公房/商品房
	feature4 = base2info.split("label")[4].split("span")[1].split("<")[0].split(">")[1]     #商住两用
        #是否独家
        bases3 = sel.xpath('//div[@class="tags clear"]/div[@class="content"]').extract()
        feature5 = ""
        for each in bases3:
            if each.find('/tt1/') != -1:
                feature5 = each.encode("GBK").split('/tt1/">')[1].split("<")[0]
        feature += feature5
        feature += "."
        feature += feature1
        feature += "."
        feature += feature2
        feature += "."
        feature += feature3
        feature_remark = feature3[4:len(feature3)].decode("GBK")
        feature4 = feature4.decode("GBK")

        if(age >= 1992) and (floor_remark != u"地下室") and (price <= 200) and (feature4 != u"商住两用"):

            #序号：
            no += 1
            print(no)

            #房源编号
            number = sel.xpath('//div[@class="houseRecord"]/span[@class="info"]').extract()
            number = str(number)
            number = number.split(">")[1].split('\\')[0]
	    fast_link = "http://bj.lianjia.com/ershoufang/"+ number + ".html"



            #房屋户型
            style = str(baseinfo).split("label")[1].split("span")[1].split("<")[0].split(">")[1]          
         
            #面积
            area = str(baseinfo).split("label")[3].split("span")[1].split("<")[0].split(">")[1]
            temp2 = ""
            area2 = ''
            temp2 = area[0:len(area)]
            for a in temp2:
                if(a.isdigit() == True) or (a == "."):
                    area2 += a
            area2 = float(area2)

            #朝向
            orientation = str(baseinfo).split("label")[7].split("span")[1].split("<")[0].split(">")[1]

            #建筑类型
            building_type = str(baseinfo).split("label")[6].split("span")[1].split("<")[0].split(">")[1]
            
            #梯户比例
            elevator = str(baseinfo).split("label")[8].split("span")[1].split("<")[0].split(">")[1]

            #供暖方式
            heating = str(baseinfo).split("label")[10].split("span")[1].split("<")[0].split(">")[1]

            #装修情况
            decoration = str(baseinfo).split("label")[9].split("span")[1].split("<")[0].split(">")[1]

            #小区名称
            community = sel.xpath('//div[@class="communityName"]/a[@class="info"]').extract()
            for each in community:
                each = each.split(">")[1].split("<")[0]
            community = each.encode("GBK")

            #所在区域
            around = sel.xpath('//div[@class="areaName"]/span[@class="info"]').extract()
            print(around)
            for each in around:
                a = each.split("blank")[1].split(">")[1].split("<")[0]
                a += "."
                a += each.split("blank")[2].split(">")[1].split("<")[0]
                a += "."
            around = a
            arounds = sel.xpath('//div[@class="areaName"]/a').extract()
            for each in arounds:
                a = each.split("title=")[1].split('"')[1]
            around += a
            around = around.encode("GBK")

            #贷款
            #贷款年限(loan_period)、总价(total)、首付(down_payment)、税费(tax)、月供(monthly)
            loan_period1 = 47 - (2016-age)
            if loan_period1 >= 30:
                loan_period1 = 30
            loan_period2 = 57 - (2016-age)
            if loan_period2 >= 30:
                loan_period2 = 30
            loan_period = ""
            loan_period += str(loan_period1)
            loan_period += "/"
            loan_period += str(loan_period2)
            #税费
            assess_price = price * 0.85
            loan_total = assess_price * 0.80
            original_value = 100      #假设原值70W
            if price <= 130:
                original_value = 60
            if loan_total >= 120:
                loan_total = 120
                assess_price = 150
            qi_tax = assess_price * 0.01
            ge_tax = 0
            gong_tax = 0
            jing_tax = 0
            
            if (feature1.decode("GBK") == u"满二年") or (feature1.decode("GBK") == u"暂无数据"):
                ge_tax = (assess_price - original_value)*0.2
            if (feature2.decode("GBK") == u"不唯一住宅"):
                ge_tax += assess_price * 0.01
            if (feature3.decode("GBK") == u"已购公房"):
                gong_tax = 15.6*7*area2/10000
            if (feature_remark == u"经济适用房"):
                jing_tax = (assess_price - original_value) * 0.1
            tax = float('%0.1f' %(qi_tax + ge_tax + gong_tax + jing_tax))
            #手续费
            agency_fee = 0.027 * price
            assess_fee = 0.15
            guarantee_fee = 0.36
            fee = float('%0.1f' %(agency_fee + assess_fee + guarantee_fee))
            #总价
            total = float('%0.1f' %(price + tax + fee))
            #首付
            down_payment = float('%0.1f' %(price - loan_total + fee + tax))
           
            #---------调试代码--START------------
            #print(type(bases))
            #print(isinstance(style, unicode))
            '''
            f = open('spider2.json','w')
            print("++++++*************++++++++")
            f.write(unit_price)
            print(style)
            f.close()
            print("zzzzzzzzzz")
            '''
            #----------调试代码--END-------------    
            global number_global
	    flag = "False"
	    for each in number_global:
		if each == number:
			flag = "True"
			break
	    if flag != "True":
		number_global.append(number)
                item['number'] = number
		item['fast_link'] = fast_link
                item['style'] = style
                item['floor'] = floor
                item['area'] = area
                item['age'] = age
                item['orientation'] = orientation
                item['building_type'] = building_type
                item['elevator'] = elevator
                item['price'] = price
                item['heating'] = heating
                item['decoration'] = decoration
                item['unit_price'] = unit_price
                item['feature'] = feature
                item['no'] = no
                item['loan_period'] = loan_period
                item['tax'] = tax
                item['total'] = total
                item['down_payment'] = down_payment
                item['community'] = community
                item['around'] = around
                items.append(item)
                return items


