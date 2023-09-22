import tkinter 
import speedtest

#---config The windo----
windo = tkinter.Tk()
windo.geometry("750x700")
windo.title("Speedtest")

#----start function----
def start():
    st = speedtest.Speedtest(secure=True)
    st.get_servers()
    best = st.get_best_server()
    download_test = st.download()
    upload_test = st.upload()
    download_speed = round(download_test / (10**6),2)
    uplaod_speed = round(upload_test / (10**6),2)
    label2.config(text=f"Downlaod : {download_speed} MB/s")
    label3.config(text=f"Upload : {upload_test} MB/s")

#-----labels and button----
label1 = tkinter.Label(windo, text="Welcome to speedtest",font=("Helvetica", 25))
label1.pack(pady=45)
button1 = tkinter.Button(windo, text="start", command=start, width=40)
button1.pack(pady=50)
label2 = tkinter.Label(windo, text="", font=("Helvetica", 15), fg="red")
label2.pack(pady=55)
label3 = tkinter.Label(windo, text="", font=("Helvetica", 15),fg="blue")
label3.pack(pady=55)

#---mainloop----
windo.mainloop()
