# Cloudshare usecase and other recommendation engines
# Cloudshare 用例和其它推荐引擎

## Cloudshare data stream
## Cloudshare 数据流

The project willendare has three parts of the data about recommendation,  uploads\SCRAPPY
and JD, they correspond to the model, sims and requirement.

在Willendare简历推荐系统中有三种数据流和其中的推荐系统密切相关, 包括上传、爬取 和 JD，
它们和模型，相似点 和需求.

    - The repo and storage is assemblage, give dimension and requirement
      to get recommended articles. 
    - The customer can adjust his assemblage.
    - Fix or customized the dimension is not the most important thing.
      Depends on how to use\resources consumed and user group.
    - Most of the service Project features is about project management.

    - Repo和storage是混杂的数据集，给出维度和需求能获得被推荐的文章。
    - 用户能微调数据集
    - 究竟维度是否固定并不是设计时决定的。取决于面向的用户群和系统能承受多少资源消耗
    - Project服务中的特性主要为项目管理服务。

## Cloudshare processing
## Cloudshare 处理过程

    Model         -    Sims        -    Inupt          -    Results
    Dimension     -    Assemblage  -    Requirement    -    Results
    维度           -    数据集       -    需求            -    结果
    What you want -    Mass data   -    What you want  -    What you want

Each dimension belonging to the same association set. We can only one dimension
from an association set. Regardless of the size of the input data, the sims is only sensitive
to the dimensions of the model. Here can give some examples:

每个维度下的词句集合方向性必须是一致的。无论提供的文章与该维度多麽无关，只会获得
与该维度吻合的相似点.这里是一些例子:

    Input Painting|Artist|Theme to build a model，
    Use Oil painting appreciation passages to make sims，
    Put themes then get a genre of paintings passage.

    Input Book|Theme|Category to build a model,
    Use books overview to make sims,
    Put interested topics then get the books you might be interested in 。

 And a counterexample:
 和一个反例:

    Input Mobile phone Brand|Performance|Evaluation to build a model,
    Use Mobile evaluation articles to make sims,
    Put rating and performance requirements get phones.

In  current CV recommendation idea:
现在的简历推荐模型想法：

    UploadCV      -    CV          -    JD/CV          -    CV
    
In fact, the source of our model is:
事实上，我们使用这些数据来建立我们的匹配系统模型：

    Input education|gender|marital status|company|position|experience
    to build a model.
    Use education|gender|marital status|company|position|experience
    to make sims.
    Put education|skills|experience|working conditions get People(CV).

1) Put too many different dimensions of information in the same model.
2) Our requirements and models are asymmetric.

1）在一个模型中输入太多不同维度的信息
2）我们的需求和模型是不对称的

I design conditions to find a person:
为寻找指定的人我设计了一些条件：

    - Education
    - Skills
    - Position
    - Industry
    - Licensing requirements

    Input these 5 dimensions words to  build 5 model.
    Use education|gender|marital status|company|position|experience
    to make sims.
    According to the requirements, listed in different dimensions of
    the demand to use different models to filter unqualified people.

## Douban movie
## 豆瓣电影

Douban is a information aggregation website,  and it can provide other films related to
the film you are viewing.

I can be sure that they used a very long time to improve and polish the recommendation
system, do not analyze  the implementation method, but can know the principles of its mode
from the recommended results:

豆瓣是一个信息集合网站，它其中一个功能是提供你看过电影的相关电影。
我能肯定它使用了很长的时间去打磨优化它的推荐系统，但如果我们忽略它具体算法策略
可以由推荐结果知道它推荐的原则：

    楚门的世界 The Truman Show (1998) [9.0]
    People who like the movie also like it：
    - 辛德勒的名单 Schindler's List (1993) [9.4]
    - 飞越疯人院 One Flew Over the Cuckoo's Nest (1975) [9.0]
    - 拯救大兵瑞恩 Saving Private Ryan (1998) [8.8]
    - 闻香识女人 Scent of a Woman (1992) [8.9]
    - 肖申克的救赎 The Shawshank Redemption (1994) [9.6]
    - 这个杀手不太冷 Léon (1994) [9.4]
    
According to the title, User Generated Content(UGC) mode is the most important dimensions.
These recommendations are high score movies, not base on film topics.
根据“喜欢该电影的人同时也喜欢”， 用户提供内容模式是它最重要的维度。
它推荐的全部是高分电影，与题材无关。

    异形4 Alien: Resurrection (1997) [7.5]
    People who like the movie also like it：
    - 异形3 Alien³ (1992) [7.1]
    - 侏罗纪公园2：失落的世界 The Lost World: Jurassic Park (1997) [7.4]
    - 星河战队 Starship Troopers (1997) [7.6]
    - 铁血战士 Predator (1987) [7.5]
    - 生化危机 Resident Evil (2002) [7.8]
    - 终结者3 Terminator 3: Rise of the Machines (2003) [7.0]
    - 普罗米修斯 Prometheus (2012) [7.1]
    - 我是传奇 I Am Legend (2007) [7.8]

These are science fiction movies, we can also find that the scores of these films are close.
So I think one of the model is:
这些推荐都是科幻类的电影，我们同时可以发现这些电影的评分接近。
根据这些我可以推测它的模型：

    Input theme|scores|other movies that people like to watch to build a model.
    Use movie themes make sims.
    Put theme|scores get Movies.

Here two important point:

1) Not need to import the GB level video file to train the model.
2) They have leading man\leading lady\director\Screenwriter,
    but these things did not play a leading role in the recommendation.

在此有两个重点：

1）系统不需要输入数个G的电影视频文件来训练模型
2）它拥有男、女主角、导演、制片人的数据，但这些数据并没有在推荐结果中体现出来。

## Apply to Sourfish
## 在Sourfish中的应用

Sourfish is a Crawler - search engine -GUI application. The data flow model is
Assemblage - Model - GUI. Because the instance provide services for only one
company, so hide the dimension and requirement  part.
Sourfish是一个爬取-搜索引擎-用户界面的联合应用。它的数据流程是
数据集-模型-界面。因为我们当前只有一个用户，所以它的维度和需求是隐藏的。
 
One of the applications based on cloudshare design：
这里有一个基于cloudshare推荐设计的应用：

    Customers input interested website and crawl rules to be Assemblage.
    Provide tendering/bidding/project size/involving company departments model.
    Put the bidding conditions and involving departments can obtain the latest
    relevant announcement.

The fact it is similar to use search engine and classification system, but fuzzy keyword
matching when we build model.
这个例子有点类似于搜索引擎与分类器结合，在建立模型的阶段确立敏感关键字。

## Knowledge engine
## 知识引擎

I have been work in a project which want to help users understand something he wants to know
but the information is asymmetric or do not know how to start, it is hard to finish due to
the solution is base on search engine and extremely simplified user configuration\key word
system, I think using cloudshare can complete the demand (of course on branch
master cloudshare some resume matching methods  coupling is strong)

我曾经做过一个项目， 关于帮助用户获取消息不对称信息和学习不知从何下手的知识，
由于基于搜索引擎的设计和k-v系统的用户配置局限性导致不能实现满足需求的解决方案，
我认为使用cloudshare的设计能完成该部分需求（当然在此之前需要一些有关简历匹配系统
的解耦合）

Assemblage is from RSS or News, articles, wiki, scraping tool.
Customers choose several dimension combination form of words as models.
The dimension words can be customized or from some download corpus provided from us.
Customers input some keywords as requirement. Then they get related articles.

数据集来源于维基百科，新闻爬取，RSS订阅。
用户选择几个维度的词汇组合，以此作为匹配基准。
这些维度的词汇可以定制或者来自于我们提供的下载词库。
用户输入一些需求关键字，然后他们得到相关的文章。

Some examples:

- Selected dimension
 1. All kinds of art description of subject
 2. The movie circle
Input an movie article, get films with the same theme and related producer.

- 选择维度
 1. 各种各样的艺术主题的描述
 2. 电影圈
 输入一篇电影文章，获取类似主题与改影片相关人物的其它电影文章

- Selected dimension
 1. The theme of the health care keeping
 2. Rumors and myth
 3. Food
 Input some kind of food can the food on the health effects of some wrong views.

- 选择维度
 1. 养生保健
 2. 流言与谣言
 3. 食品
 输入一些食物，获取该食物对身体健康影响的一些谣言。

Search engine can find something that you know, have too specific direction at the
same time, it can't meet the black swans.
Search engine can find something identity is known to all, but we will pay more attention
to less people know or different points of view. Like shopping, we want to focus on more 'bad' review rather than the 'good'.
The design dimension of separation can easy to find out differently and alternative points of view
in big data .

搜索引擎能找到你明确知道的东西，同时有太具体的方向性，它不能满足黑天鹅事件。
搜素引擎能找到大家都知道或者认同的东西，但有时我们会更关注少人知道的或者方向的观点，
就像购物时我们更想关注差评的内容而非好评。
该设计下的维度分离能在大数据中容易找出不同的看法和另类的观点。
