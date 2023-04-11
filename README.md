# ZADANIE 1: Konfiguracja oprogramowania

## Pozadanie 1: Dlaczego zdecydowałam się wziąć udział w wyzwaniu Dare IT Challenge?
#### Hej! Jestem Zuza i jako tester manualny pracuję pół roku, chcę dalej rozwijać swoje umiejętności, dlatego dołączyłam do tego wyzwania. Chcę się nauczyć podstaw automatyzacji testów oraz przekonać się czy Python+Selenium to połączenie, które będzie mi odpowiadało w pracy. 

# ZADANIE 2: Selektory

## Subtask 2: Wyszukiwanie selektorów na stronie logowania. Wymień wszystkie elementy, które znajdują się na stronie logowania.
#### **Pole do wpisania loginu:**
![image](https://user-images.githubusercontent.com/36918613/231254123-08d44da0-34c8-4474-b190-3a12c43c212e.png)

1. //*[@id="login"] 
2. /html/body/div/form/div/div[1]/div[1]/div/input
3. //*[text()="Login"]

#### **Pole do wpisania hasła:**
![image](https://user-images.githubusercontent.com/36918613/231254473-7ea180fa-847d-4186-9619-24973a09476f.png)

1. //*[@id="password"]
2. /html/body/div/form/div/div[1]/div[2]/div/input
3. //*[text()="Password"] 

#### **Przypomnienie hasła:**
![image](https://user-images.githubusercontent.com/36918613/231256083-00e67464-f8b1-4299-946c-54cc259429c2.png)

1. //*[@id="__next"]/form/div/div[1]/a
2. /html/body/div/form/div/div[1]/a
3. //*[contains(@class, "MuiTypography-root MuiLink")]  

#### **Przycisk logowania:**
![image](https://user-images.githubusercontent.com/36918613/231256210-99690b62-3d96-4138-a2fd-b14a9aa11bfc.png)

1. //*[@id="__next"]/form/div/div[2]/button/span[1]
2. /html/body/div/form/div/div[2]/button/span[1]
3. //*[text()="Sign in"]

#### **Przycisk zmiany języka:**
![image](https://user-images.githubusercontent.com/36918613/231257042-752125c9-5a1d-4c2a-90cb-399d0e3442b5.png)

1. //*[@id="__next"]/form/div/div[2]/div/div
2. /html/body/div/form/div/div[2]/div/div
3. //*[text()="English"]

