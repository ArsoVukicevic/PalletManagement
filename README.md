# Warehouse 4.0 solution for the pallet management in SMEs with QR-code, machine vision and IP cameras: A use-case from the printing industry

Transport of products and raw materials with forklifts and pallets still underpins the majority of material flow in the global chain supply. Moreover, many companies record losses due to the operators’ inability to timely manage large amounts of pallets. As a use-case, this study considered the needs of a SME from the printing industry - since there are a large number of raw materials that need to be transported during the production process. The aim of this study was to propose and assess an affordable solution for the pallet management with QR code,  open-source software tools and conventional surveillance equipment. 

![](GUI%20code/images/01%20Overview.jpg)

Although one may find concerns in literature (which question the usage of QR in logistics), we report that QR-based technology is suitable for the particular use-case, since pallets are static in the inter-warehouse. The reliability was achieved by using multiple IP cameras, which ensures that if one camera fails to detect QR code another one will compensate it. Since surveillance technology is evolving fast and it is becoming more affordable, we conclude that more attention needs to be invested into investigation and adaptation of such technologies to fit the needs of SMEs (since they generate the most of workplaces and GDP in developed countries - but commonly can not afford complex and expensive solutions available on the market). 

![](GUI%20code/images/02%20Architecture%20and%20workflow.jpg)
Software architecture and UML Workflow diagram of the proposed solution.



Keywords: Pallets, Logistics 4.0, QR code, Computer vision, Warehouse 4.0

# Instructions
Run GrafostilGUI.py - links for instllation of requsted libraries are placed within the code

Import libraries:

    from arsGrafostilBiblioteka import *
    import cv2 as cv

Set-up camera address and read image: 

     ipAddress = 'rtsp://admin:password@IP_addrss:port/cam/realmonitor?channel=1@subtype=0' #shape:(2160, 3840, 3)  # IP camera
     ipAddress = 0# USB camera
     cap       = cv.VideoCapture(ipAddress)
     return_value, image = cap.read()

Generate and print QR code: 

    data      = '0044,04/33'
    testQRimg = generateQR(data, False)
    printQqCodeOnWinPrinter(testQRimg, False)
    data, locations = readQRcode(testQRimg, False)    
    cv.imwrite('img1.jpg',testQRimg) # save image // open and read it with i.e. mobile phone

Live demo on the single camera: 

    import  matplotlib.pyplot as plt
    plt.ion()
    fig = plt.figure(facecolor='white')
    while True:
        img, bzv = cap.read()
        data, locations = readQRcode(img, False)
        plt.clf()
        plt.imshow(img)
        for i in range(len(data)):
            plt.text(locations[i][0].x, lokacijePodataka[i][0].y, data[i], horizontalalignment='left', fontsize=16)
            rectangle = plt.Polygon(locations[i],closed=True, fill=None, edgecolor='r')
            plt.gca().add_patch(rectangle)
        fig.canvas.draw()
        fig.canvas.flush_events()   
