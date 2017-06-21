# pyWager
run simulation of wager use python

这个项目是用来模拟赌博和投资/投机的；模拟各种参赌策略是否有效，如何取得最大化收益：  </br>

1） 赌徒谬误的策略（如果赢了就收手，如果输了就加倍赌注直到嬴）是否真的(P=0.5情况下)是否真的能赢钱？ </br>
2） P=0.5情况下，钱款无数（也就是把别人都吸干了），是否能赢钱？  </br>
3） P<0.5情况下，有没可能赢钱？   </br>

-----------------------------------------------------------------------------------

结论是： </br>
1）去赌场的人基本都是傻子（除了几个数学家之外），他们要么不太了解数学，要么没有了解本程序； </br>
2）只有P>0.5才是赢钱的唯一通道； </br>
3）仿真甚至统一了股票里面长期争议的“价投”和“投机”的投资方法，认为他们都是赌博，不过前者赢率>0.5，后者不一定（自认为是猎手的也会偶尔沦为猎物）。这点我问过一个大师，大师不屑，说这点我早就说过了，价投是赢大概率的钱，投机是不确定。 </br>

结论很简洁：不要在P<=0.5的情况下参赌。 </br>

-----------------------------------------------------------------------------------
TODO: </br>
1) 目前模拟方式是利用微信红包牛牛赌法；牛牛赌法赔率变化比较大，所以缺陷是貌似贝利下注法不能直接用，需要一个改进版； </br>
2) 更多的策略验证： </br>
    A) P=0.5的情况下  </br>
    策略1）：每天赢20%就收手，输了继续赌，日日如此，是否一定赢钱？（假设手里资金无限，但是每日参赌次数有限，因为只有24小时） </br>
    策略2）：上条策略基础上，赌资限额（比如2万） </br>
    策略3）：假设赌资不限额，但是别的20个固定玩家赌资有限（比如20万），他们输光了就会退出。那么这种情况下是否长期赌下去，别人的钱输光了，是否就会赢？ </br>

    B）引入干扰的情况下，也就是P>0.5（比如0.56）的情况下 </br>
    策略1）：验证贝利下注法是否比其它下注方式更有效 </br>
    策略2）：贝利下注本身不会引起输光的情况，但是微信玩法不一样（赔率不固定，你有可能一次输光），在资金有限的情况下，长期使用贝利下注，是否一定赢钱？ </br>


------------------------------------------------------------------------------------
2017.6.21: upload to github </br>
2016.6: init version </br>
