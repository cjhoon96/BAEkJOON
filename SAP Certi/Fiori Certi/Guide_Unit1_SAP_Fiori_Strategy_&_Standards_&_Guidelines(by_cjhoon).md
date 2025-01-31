# 1. SAP Fiori Strategy, Standards and Guidelines

#### UX402 / UX400, UX403



## UX 410 Unit 1, 2, 3, 4, 5

## Define SAP Fiori Key principles

* ### UX 의 중요성

  * **Business Value**
    * 생산성 / Data 퀄리티 향상
    * 교육 비용 / change request / user error 절감
  * **Human Value**
    * user 만족도 / customer loyalty / solution adoption 증가
    * Reduce function between IT and business around UX issues / Strengthen Relationship (IT / Business)



* ### UX Design Service

  * Design Strategy
  * New / Renew / Empower (UX Strategy)
  * Architecture and Technology



* ### UX Design

  * Visual design

  * Information architecture

  * Interaction Design

  * Usability

  * Accessibility

  * Human-computer interaction



* ### SAP Fiori 주요 설계 원칙

  * #### Role-based apps

  * #### Adaptive

  * #### Simple

  * #### Coherent

  * #### Delightful



* ### Impact of Fiori 

  * Business

    * digitalization

    * simplification

    * re-imagination of processes
    
    * Cloud readiness
  
  
    * User	
  
      * 사용자 중심
  
      * 디자인 중심 개발
  
      * 모든 SAP 솔루션에서 공통된 UX
  
  
    * Technology
  
      * 웹 및 개방형 표준
  
      * 서비스 지향
  
      * 인메모리 및 클라우드 컴퓨팅
      
      * 모바일 기술
  



* ### De-composition and Re-composition

  SAP Fiori 애플리케이션은 하나의 크고 복잡한 SAP 트랜잭션의 기능을 여러 Fiori 애플리케이션으로 분해할 수 있다. 이를 **<u>De-composition</u>** 이라 한다. 

  여러 SAP 트랜잭션의 기능을 결합하여 전체 비즈니스 트랜잭션을 수행하는 SAP Fiori 애플리케이션을 만들 수도 있다. 이를 **<u>Re-composition</u>** 이라 한다.

  SAP Fiori app 을 설계할 때는 system 이 고려 대상이 되는 경우는 거의 없다.오히려 사용자 중심적이다.

  * #### Re-composition 

    SAP Fiori app 을 사용하면 GUI 의 여러 Transaction 의 기능을 결합하여 기능을 구축할 수 있다.

    **<u>사용자 탐색의 감소</u> / <u>화면 상호 작용의 단순화</u>**

    **=> 사용자 생산성 향상**

  * #### De-composition

    다른 Role 을 가진 많은 사용자가 사용하는 일반적인 T-Code 는 각 Role에 대해 여러 앱으로 분할 될 수 있다. 

    SAP Fiori 는 Role-based 이기 때문에 사용자가 업무와 필요에 따라 작업을 수행할 수 있도록 필요한 화면 요소만 제공

    **=> <u>사용자 집중력 유지</u> / <u>효율적인 작업</u>** 



## The concept of Design Thinking

* ### Design-Led Development (DLD)

  * #### Problem Space

    * #### Discover

      * Scope
      * Research
      * Synthesize

  * #### Solution Space

    * #### Design

      * Ideate
      * Prototype
      * Validate

    * #### Develop

      * Implement
      * Test
      * Deploy





## SPA Fiori Demension 

* ### Concept

  * Role-based
  * Adaptive
  * Coherent
  * Simple
  * Delightful

* ### Design

  * Visual Design
  * Information Architecture
  * Interaction Patterns

* ### Technology



## SAP Fiori application types

* ### Transactional

  Task based 이며 business process 를 수행한다.

  <u>**CRUD 작업중 하나 이상이**</u> 있으며 app 과 back-end 간에 양방향 데이터 이동을 수반한다.

  <u>**SAP HANA DB 가 필수는 아니지만 최적의 성능을 위해 권장한다.**</u>

  * SAP Fiori Element
    * Overview Page
    * List Report
    * Worklist
  * Classic Application
    * ABAP Transaction
    * WebClient UI
    * Web Dynpro ABAP



* ### Analytical

  **읽기 전용 앱**으로 일반적으로 SAP HANA 의 기능을 사용하여 **숫자 <u>크런칭, 데이터 시각화, 미래 예측</u>** 등의 사용 사례를 해결한다.

  SAP 에서 제공되는 <u>**KPI Modeler**</u> 를 사용하여 **<u>프로그래밍 없이 KPI 그래프/차트</u>** 를 생성할 수 있다.

  **<u>기본 제공되는 KPI</u>** 도 존재한다.

  <u>**SAP HANA 가 데이터베이스로 필요하다.**</u>

  * SAP Fiori Element
    * Overview Page
    * Analytical List Page
  * BW Query Used
    * Analytics Cloud
    * Design Studio
    * Web Dynpro ABAP



* ### Fact Sheet

  Business object 또는 Business transaction 에 대한 **<u>상황별 정보를 표시</u>**한다.

  이 앱들은 보통 <u>**실행 타일이 없다.**</u>

  대신 <u>검색 결과를 클릭</u>하거나 다른 <u>**Transactional / Analytical / Fact Sheet App 에서**</u> 사용할 수 있는 다양한 **<u>드릴다운 링크를 클릭하여 실행</u>**된다.

  다른 Transactional app 에 대한 링크도 제공한다.

  (ex. 구매 주문 정보 시트 앱에서 구매 요청을 구매 주문으로 변환하는 트랜잭션 앱으로 이동할 수 있다.)

  **<u>읽기 전용 앱</u>**으로 데이터를 ***<u>CDS view 로 보며 UI rendering annotation</u>*** 을 사용한다.

  **<u>SAP HANA 가 데이터베이스로 필요하다.</u>**

  * SAP Fiori Element
    * Overview Page
    * Object Page





## Elements of User Experience Design



## Implement SAP Fiori UIs using the SAP Fiori Design Guidelines





























































## Practice

#### What impact does UX have on monetary values? 

#### (Choose the correct answers). 

Increases user satisfaction. 

Provides productivity gains and increases data quality. 

Strengthens relationships with customers. 

Provides training cost savings 

Reduces the number of change requests and user errors.

****

:book: UX402 - Unit 1

bcd

****



#### What is the principle of SAP UX strategy? 

#### (Choose the correct answer). 

Design Strategy 

New, Renew, Enablement 

New, Renew, Empower 

Architecture and Technology 

SAP Screen Personas.

****

:book: UX402 - Unit 1 

c

https://www.eventservice.kr/2017/sap/00/file/2017_2pm_0405_Session.pdf

****



#### What impact does SAP Fiori have on business? 

#### (Choose the correct answers). 

Digitalization 

Simplification 

Support the web and open standards 

Provides a user-centered approach 

Leads to re-imagination of processes.

****

:book: UX402 - Unit 1

abe

Business

* digitalization
* simplification
* re-imagination of processes

User

* 사용자 중심
* 디자인 중심 개발
* 모든 SAP 솔루션에서 공통된 UX

Technology

* 웹 및 개방형 표준
* 서비스 지향
* 인메모리 및 클라우드 컴퓨팅

****



#### Which of the following are the current SAP UI Tools? 

#### (Choose the correct answers). 

SAPUI5 Application Development Tools 

SAP Screen Personas 

SAP NetWeaver Portal 

Flexible UI Designer 

SAP NetWeaver Gateway.

****

:book: UX402 - Unit 1

abd

****









#### What are the SAP Fiori principles? (Choose the correct answers). 

### Role-based 

### Adaptive 

Creative 

### Coherent 

Complex.

****

:book: UX402 - Unit 1

https://experience.sap.com/fiori-design-web/design-principles/

**Role-based** 

**Adaptive (적응형)**

**Coherent (일관성)**

**Simple (단순성)**

**Delightful**

****













#### What are the goals of the SAPUI5 framework? (Choose the correct answers). 

### Provide a user interface technology for building and adapting client applications. 

Provide a user interface technology for building and adapting server-based applications. 

Provide a lightweight programming model for desktop only applications 

### Provide an extensible framework for building desktop and mobile applications.

****

:book: UX402 - Unit 1

****





#### Which of the following steps are part of the design phase in the DLD? 

다음 중 DLD의 design 단계의 일부인 단계는?

## (Choose the correct answers). 

Test 

### Validate 

### Prototype 

Scope 

### Ideate

****

:book: UX402 - Unit 1

https://experience.sap.com/fiori-design-web/design-led-development-process-external/

https://blogs.sap.com/2017/03/01/good-things-come-in-3s-intro-to-the-dld-process/

**DLD 의 세가지 단계**

* **Discover**
  * Scope
  * 360° Research
  * Synthesize
* **Design**
  * ideate
  * Prototype
  * validate
* **Deliver**
  * implement
  * Test
  * Deploy

DLD = **D**esign-**l**ed **d**evelopment

개발 프로세스이다.

****





#### Which of the following steps are part of the discover phase in the DLD? (Choose the correct answers). 

### Scope 

Test 

Implement 

### Research 

### Synthesize.

****

:book: UX402 - Unit 1

https://blogs.sap.com/2017/03/01/good-things-come-in-3s-intro-to-the-dld-process/

****







#### What are the current UI Technologies of SAP? 

#### (Choose the correct answers). 

Business Server Pages 

### SAPUI5 

Java Server Pages 

### Web Dynpro ABAP / Floorplan Manager 

### Dynpro.

****

:book: UX402 - Unit 1

https://help.sap.com/doc/saphelp_nw74/7.4.16/en-us/4f/47faaced4b49e985dd31298bd3775f/frameset.htm

****



