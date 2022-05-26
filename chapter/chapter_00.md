# CHAPTER 00 서론

## 0.1 알고리즘의 역할

컴퓨터과학의 가장 근본적인 개념  
나눗셈법 알고리즘, 유클리드 호제법 알고리즘   
어떤 문제의 해결을 위한 알고리즘이 존재하지 않는다면 그 문제의 해결은 컴퓨터의 능력 밖이다.  

알고리즘의 한계를 밝히는 연구 = 괴델의 불완전성 정리 = 알고리즘으로 해결할 수 없는 산술 문제가 존재한다.  
이러한 자각에서 파생된 알고리즘의 한계에 대한 연구가 컴퓨터과학이라는 학문의 효시가 되었다.  
실상 컴퓨터과학의 핵심은 알고리즘에 대한 연구다.

## 0.2 컴퓨터의 기원

### 19c 이전

주판(고대) → 파스칼의 덧셈 계산기(17c) → 라이프니츠의 다양한 연산이 추가된 계산기(18c) → 배비지의 차분 엔진(19c)

파스칼과 라이프니츠의 계산기는 계산 알고리즘이 계산기 안에 고정되어있다.  
반면, 배비지의 차분 엔진은 여러 계산을 수행하기 위해 변경될 수 있었다.   

배비지가 고안한 계산기는 현대 컴퓨터의 선조라고 할 수 있다.  
차분 엔진은 '연속적 차분 값'을 계산하여 숫자값을 결정하였다.  
연속적 차분의 예시로 정수 제곱의 계산을 살펴보면, 각 제곱값의 2차 차분은 모두 2로 동일하다.  
이는 y=x²의 미분이 기울기가 2인 직선이 된다는 사실에 기초한다.

배비지의 해석 엔진은 프로그램이 가능한 계산기였지만 제작비용을 지원받지 못했다.  
해당 엔진은 종이 카드에 뚫은 구멍들을 이용하여 명령을 읽을 수 있도록 설계되었다.  

최초의 프로그래머로 지목되는 에이다는 배비지의 해석 엔진에서 여러가지 계산을 수행하기 위해  
어떻게 프로그램을 작성할 수 있는지를 보이는 논문을 출간한 바 있다.

구멍 있는 종이카드를 사용하여 알고리즘을 표현하는 아이디어는 배비지가 창안한 것은 아니다.  
자카드 직조기에서 처음 등장했던 것을 배비지가 응용한 것이다.  

이 아이디어를 잘 활용한 또다른 사람은 홀러리스다.  
홀러리스는 도표화 작업속도를 향상시키기 위해 종이카드 구멍들로 정보를 표현하는 방법을 사용했다.  
후에 IBM이라는 회사의 설립에 이 작업이 큰 영향을 주었다.  

이 카드는 후에 천공카드(Punched card)라 불리게 되며, 1970년대까지 컴퓨터에 정보를 전달하는 수단으로 이용되었다.

19c의 기술은 발명된 계산기들을 실용적인 비용으로 생산할 정도의 수준에 이르지 못했다.  
이러한 문제는 20c 초반 전자공학의 발전과 함께 극복되었다.  

### 20c 이후

벨연구소 스티비츠의 전자-기계 혼용식 계산기(1940) → 하버드 에이큰과 IBM 공학자들의 마크I(1944)

이 계산기들은 전자적으로 제어되는 많은 개수의 기계식 릴레이를 이용하였다.  
이에 금방 다른 학자들이 진공관 기술을 응용하여 순수 전자식 컴퓨터를 제작하며 사실상 금세 쓸모가 없어졌다.  

순수 전자식 컴퓨터의 효시는 아이오와 주립대 아타나소프와 베리가 제작한 아타나소프-베리 컴퓨터다.  
또다른 전자식 컴퓨터로는 2차 세계대전 후반 독일군의 암호문 해독을 위해 영국에서 제작된 콜로서스라는 컴퓨터가 있다.  
(실제 이러한 컴퓨터들이 10여개가 더 있는데, 군사기밀 및 국가안보등의 이유로 존재가 감추어져 컴퓨터 족보에 포함되지 않고 있었다.)

이들보다 발전된 컴퓨터들이 곧 뒤따랐다.  
펜실베니아대 무어전기공학부 모클리와 에커트의 ENIAC(Electronic Numerical Integrator And Computer)이 여기 포함된다.  

전자식 컴퓨터가 나타난 이래, 컴퓨터의 역사는 트랜지스터의 발명이나 그 후 직접 회로 개발등을 포함하는 기술 발전과 밀접한 관련을 맺고 있다.  

집적 회로는 완전한 회로를 하나의 장치로 만든 것으로,  
1940년대에는 하나의 방을 차지했던 컴퓨터가 지금의 작은 상자 크기까지 줄어들 수 있게 했다.  
이와 동시에 컴퓨터의 처리 능력은 2년마다 두배씩 발전해왔으며 이러한 발전은 오늘날까지도 계속되고 있다.  

### 컴퓨터의 보급

컴퓨터 보급에 결정적 역할을 한 것은 데스크톱 컴퓨터의 개발이다.  
그 기원은 집에서 칩들을 조합하여 컴퓨터를 자체 제작하였던 컴퓨터 취미생활자들에게서 찾을 수 있다.  
그렇게 탄생한 것이 1976년 설립된 스티브 잡스와 스티븐 워즈니악의 애플사다.  
그외 유사한 회사들에는 코모도어, 히쓰키트, 라디오섁 등이 있었는데,  
비록 이러한 제품들이 언더그라운드에서는 인기를 끌었지만 기업 업무용으로 널리 쓰이지는 못했다.  
기업들에서는 대부분의 계산 업무에 이미 확고한 위치를 잡고 있는 IBM 컴퓨터를 사용하고 있었기 때문이다.  

1981년 IBM은 PC(Personal computer)라고 불리는 IBM 최초의 데스크톱 컴퓨터를 소개하였는데,  
기본 소프트웨어는 신진 기업 마이크로소프트사가 개발한 것이었다.  
PC는 즉각적인 성공을 거두며 데스크톱 컴퓨터가 기업들에서도 필수 장비가 되는 계기를 마련하였다.  
오늘날 PC라는 용어는 IBM의 초창기 데스크톱 컴퓨터의 설계를 발전시킨 모든 컴퓨터들을 가리키며,  
대부분의 PC에서는 여전히 마이크로소프트사의 소프트웨어(Windows)를 채택하고 있다.  
때로 PC는 데스크톱이나 노트북컴퓨터와 같은 의미로 사용되기도 한다.  

### 20c 후반

20세기가 끝나갈 무렵 인터넷(Internet)이라고 불리는 범세계적 시스템에  
개별 컴퓨터들을 연결할 수 있음으로 해서 통신에 획기적 전기가 마련되었다.  

이를 바탕으로 영국의 팀 버너스리는 인터넷상의 컴퓨터에 저장되어있는 문서들을 연결하여 이루어진 정보망을 구성하기 위한  
월드와이드웹(World Wide Web)이라는 시스템을 제안하였다.  
웹상의 정보들에 대한 접근을 용이하게 하기 위해 검색 엔진(Search Engine)이라는 소프트웨어 시스템이 개발되었는데,  
검색 엔진은 웹에 침투하여 발견한 정보들을 분류하고 그 결과를 사용하여 특정 주제를 조사하는 사용자들을 도와준다.  
이 분야의 주류는 구글, 야후, 마이크로소프트등이다.  

일반가정에서도 데스크톱 컴퓨터와 노트북컴퓨터들을 사용하게 되었으며, 이와 함께 컴퓨터의 소형화 기술도 계속 발전하고 있다.  
오늘날에는 초소형 컴퓨터들을 각종 전자장치 안에 내장하는 경우가 많다.  
최신 자동차들은 내장된 수십개의 소형 컴퓨터들을 이용하여 내비게이션 장치를 실행시키고 엔진 기능을 모니터링하고  
자동차오디오나 전화통신시스템을 음성으로 제어하는 서비스를 제공한다.  

컴퓨터소형화의 가장 혁신적인 분야는 휴대형 전화 기능의 확장일지 모른다.  
얼마전만해도 단순한 전화기였던 휴대형 전화는 이제 스마트폰(Smartphone)이라고 불리면서 손 안의 범용 컴퓨터로 진화하고 있다.  
실제로 많은 사람들은 PC보다 스마트폰이 사회에 미치는 영향이 더 클 것이라고 주장하고 있다.

## 0.3 본문의 구성

컴퓨터과학 학습에 대해 상향식 방식을 취하고 있다.  
컴퓨터 하드웨어와 같은 손쉬운 주제들에서 시작하여 알고리즘 복잡도나 계산가능성등과 같은 보다 추상적인 주제들로 옮겨간다.  
그 결과로 이러한 주제들에 대한 이해를 넓히면서 점점 큰 추상적 도구들을 만들어나가는 패턴을 따른다.  

**1장 데이터 저장** - 현대식 컴퓨터에서 정보를 어떻게 인코딩하고 저장하는지  
**2장 데이터 조작** - 간단한 컴퓨터의 기본 내부 동작  

**3장 운영체제** - 컴퓨터의 전반적 운영을 제어하는 소프트웨어  
**4장 네트워킹과 인터넷** - 컴퓨터 네트워크를 형성하기위해 컴퓨터들이 어떻게 서로 연결되는지, 인터넷을 형성하기위해 네트워크들이 어떻게 연결되는지  

**5장 알고리즘** - 보다 형식적인 관점에서의 알고리즘   
**6장 프로그래밍 언어** - 알고리즘의 표현과 프로그램 개발 과정  

**7장 소프트웨어 공학** - 컴퓨터과학의 한 분야, 대형 소프트웨어 시스템을 개발할 때 나타나는 문제들  

**8장 데이터 추상화** - 주기억장치 안에서 데이터조직에 사용되는 전통적 기법들, 객체지향기법에 이른 과정  
**9장 데이터베이스 시스템** - 대용량 저장장치에서 데이터조직에 전통적으로 사용되는 방법, 초대형 데이터베이스 시스템  

**10장 컴퓨터 그래픽스** - 그래픽스와 애니메이션  
**11장 인공지능** - 인간의 지능에 대한 연구  

**12장 계산이론** - 알고리즘와 컴퓨터의 한계

## 0.4 컴퓨터과학의 중심 주제

컴퓨팅이라는 분야를 폭넓게 탐색하기 위해서는 컴퓨터과학을 관통하는 중심 주제들을 유념할 필요가 있다.

### 알고리즘

오늘날 컴퓨터과학은 알고리즘 과학으로 확립되어왔다.  
알고리즘의 핵심적 역할 - 응용, 분석, 발견, 표현, 전달, 실행, 한계

1. 알고리즘적 처리과정에 의해 해결될 수 있는 것은 어떤 문제들인가?
2. 어떻게 하면 알고리즘을 보다 쉽게 찾을 수 있을 것인가?
3. 어떻게 알고리즘의 표현 및 전달을 개선할 수 있을까?
4. 서로 다른 알고리즘들의 특성들을 어떻게 분석하고 비교할 수 있을까?
5. 알고리즘은 정보처리에 어떻게 이용될 수 있는가?
6. 알고리즘은 지능적 행동의 발현에 어떻게 응용될 수 있는가?
7. 알고리즘의 응용은 사회에 어떤 영향을 미칠 것인가?

### 추상화

추상화(Abstraction)란 개체의 외적 속성과 내적 구성의 세부사항을 구별하는 것을 가리킨다.  
추상화로 인해 사용자는 장치의 내부 구성을 모르더라도 해당 장치를 사용할 수 있다.  

크고 복잡한 컴퓨터 시스템을 제작, 분석, 관리할 수 있는 것은 추상화를 적용함으로써 가능한데,  
만일 그 전체를 모두 자세히 살펴보아야 한다면 감당하기 어려울 것이다.  

각 추상 계층에서 시스템은 추상적 도구(Abstract tool)라고 불리는 구성요소들을 통해 파악할 수 있다.  
추상화를 사용함으로써 각 구성요소는 동일한 계층의 다른 구성요소들과 어떻게 상호작용하고,   
어떻게 하나로 모여 전체적으로 하나의 상위 계층 구성요소를 형성하는지등에 집중할 수 있게 된다.  
이리하여 수많은 세부사항에 빠져 헤매지 않고 당면 작업에 관계된 시스템 부분을 파악할 수 있게 된다.

### 창의성

컴퓨터는 단순한 알고리즘 명령들을 기계적으로 실행시키는 복잡한 기계일 뿐이지만,  
컴퓨터과학이라는 학문은 본질적으로 창의적인 학문이다.  
새로운 알고리즘을 발견하고 적용하는 일은 현실 세계의 문제들을 해결하기위해 도구를 사용하는  
인간의 내재된 욕구에 따른 인간 활동이다.

대규모 소프트웨어 시스템을 만드는 일은 단순한 요리법을 따라하는 일이라기보다는  
새로운 대형 조각품을 창조하는 일에 가깝다.  

### 데이터

컴퓨터는 디지털화될 수 있는 모든 정보를 표현할 수 있다.  
알고리즘은 이렇게 디지털 형태로 표현되어있는 정보들을 다양한 방식으로 처리하거나 변환시킬 수 있다.  

1. 숫자, 텍스트, 이미지, 소리, 비디오 등과 같은 일상적인 디지털 정보들을 컴퓨터에서는 어떤 형태의 데이터로 저장하는가?
2. 실세계에서 나타나는 아날로그 정보들에 관한 근사 데이터를 컴퓨터에서는 어떻게 구하는가?
3. 컴퓨터에서는 데이터상의 오류를 어떻게 탐지하고 예방하는가?
4. 우리가 접할 수 있는 데이터가 끝없이 늘어나고 상호연결성이 강화되는데 따른 파생효과는 무엇인가?

### 프로그래밍

사람의 의도를 실행가능한 컴퓨터 알고리즘으로 변환하는 일을 프로그래밍이라고 부른다.  
컴퓨터 하드웨어는 비교적 단순한 알고리즘 명령들만을 실행할 수 있지만,  
컴퓨터 프로그래밍 언어들이 제공하는 추상화를 통해 사람들은 훨씬 복잡한 문제들을 위한 해답을 추론하고 코딩할 수 있다.  

1. 프로그램은 어떻게 만드는가?
2. 어떤 종류의 오류들이 프로그램에서 발생하는가?
3. 프로그램상의 오류들을 어떻게 발견하고 고치는가?
4. 프로그램에서 오류들이 미치는 영향은 무엇인가?
5. 프로그램을 문서화하고 평가하는 방법은 무엇인가?

### 인터넷

인터넷은 전 세계의 컴퓨터들과 전자장치들을 연결하고 있으며,  
오늘날의 기술 사회에서 정보에 대한 저장, 검색, 공유 등을 수행하는 방식에 크게 영향을 미치고 있다.  
인터넷의 확산은 프라이버시와 개인정보들에 대한 보안성에도 막대한 영향을 미치고 있다.  
사이버공간은 많은 위험을 내재하고 있으며, 따라서 오늘날의 고도연결성 사회에서 암호학과 사이버보안에 대한 중요성이 점차 증대되고 있다.

### 사회적 영향

컴퓨터과학에 대한 기술적 지식만으로는 관련된 모든 문제에 대한 해결책을 제시할 수 없다.  
이러한 사실에 유념하여 컴퓨터과학의 사회적, 윤리적, 법적 영향들을 다루는 몇개의 절들을 포함한다.  
보안 문제, 소프트웨어 소유권 및 책임 문제, 데이터베이스 기술의 사회적 영향, 인공지능 발전이 가져올 결과 등이 여기 포함된다.

각 장의 끝에는 사회적 논제라는 제목 아래에 여러 질문들을 두고 있는데,  
이러한 질문들의 목적은 올바른 답으로 인도하자는 것이기보다는  
어떤 이슈에 있어서의 관련 당사자에 대한 인식, 대안들에 대한 인식,  
이러한 대안들의 단기적 파생결과와 장기적 파생 결과에 대한 인식들을 포함하여 여러 측면의 인식을 제고하자는데 있다.