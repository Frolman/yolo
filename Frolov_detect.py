#Програграмма поиска рыбы, удочки и рыбака на изображении
from ultralytics import YOLO 
import cv2

target_class=[0,1,2] #Преобученная модель имеет 3 класса
def class_detection(target_classes): # Процедура поиска определенного класса
    model = YOLO('best.pt')
    result= model.predict(
    source='fishman_1.jpg',show=True,classes=[target_classes],save=False)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
print ('Вас приветствует программа поиска рыбы, удочки и рыбака на картинке')
while True:
    vybor=int (input (f'Выберите, что будем искать?\n "1" рыбу\n "2" удочку \n "3" рыбака \n "4" Все выше \n "0" выход\n'))
    if  vybor==0:
        break
    elif vybor==1:
        class_detection(0)
    elif vybor==2:
        class_detection(1)
    elif vybor==3:
        class_detection(2)
    elif vybor==4:
        class_detection([0,1,2])
    
    
    
