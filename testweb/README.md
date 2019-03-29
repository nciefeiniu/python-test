### 接口

**启动服务前先修改 `.env` 文 件中的数据库连接**



- 模糊查询的接口：

    /api/v1/fuzzyquery/   可以用post和get请求
    
    post请求例子： 127.0.0.1:5000/api/v1/fuzzyquery/ 请求体中请携带这样的json数据 {"word": "xxx"}
    
    get 请求示例： 127.0.0.1:5000/api/v1/fuzzyquery/?word=尿囊
    
    `word`**参数是必须的！**
    

返回json数据示例：

POST 请求  http://47.103.7.89:5000/api/v1/fuzzyquery/  携带{"word": "尿囊"}
GET  请求  http://47.103.7.89:5000/api/v1/fuzzyquery/?word=尿囊
    
```json
{
   "data": [
      {
         "id": 22259,
         "name": "尿囊素铝片"
      },
      {
         "id": 72781,
         "name": "复方尿囊素片"
      },
      {
         "id": 22227,
         "name": "尿囊素铝颗粒"
      },
      {
         "id": 64577,
         "name": "硫酸锌尿囊素滴眼液"
      }
   ],
   "success": true
}
```
    
---  
    
- 药品详细信息接口
    
    /api/v1/drugs_info/    get请求
    
    例子： 127.0.0.1:5000/api/v1/drugs_info/drug_id   `drug_id`需要更换为前面模糊查询出来的id
    
    
    
返回数据示例：

http://47.103.7.89:5000/api/v1/drugs_info/22259
```json
{
   "data": {
      "Bigwarning": null,
      "English": "Aldioxa Tablets",
      "Genericnames": "尿囊素铝片",
      "Usage.": "饭前口服。成人每次0.2g（2片），每日3次，或遵医嘱。",
      "attention": "肾功能不全患者慎用。 忌与四环素类抗生素合用。 ",
      "chemical": "参见详细说明",
      "classification": "抑酸/抗反流/治疗溃疡的药物",
      "composition": "尿囊素铝",
      "da": "参见详细说明",
      "enterprise": "无锡济民可信山禾药业股份有限公司",
      "fl": "抗酸药及治疗消化性溃疡和胃肠胀气用药",
      "gs": "尿囊素铝片-无锡济民可信山禾药业股份有限公司",
      "id": 22259,
      "indications": "适用于胃及十二指肠溃疡的治疗。",
      "interaction": "忌与四环素类抗生素合用。",
      "name": "尿囊素铝片",
      "number": "国药准字H20010634",
      "reactions": "偶有便秘、稀便、口干等症状，停药后自行消失。",
      "shangp": "悉景",
      "taboo": "对本品成份过敏者禁用。 接受透析疗法的患者禁用本品。 ",
      "toxicology": "参见详细说明",
      "yaoping_id": 60515
   },
   "success": true
}
```
