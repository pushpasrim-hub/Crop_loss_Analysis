import mysql.connector
import tkinter as tk
from datetime import date
from tkinter import messagebox
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Uksri3115@",
    database="my_project"
)
if connection.is_connected():
    print("MySQL Database Connected Successfully!")
def add_farmer(name, phone, location):
    cursor = connection.cursor()
    query = """INSERT INTO Farmer (farmer_name, phone, location) VALUES (%s, %s, %s)"""
    cursor.execute(query, (name, phone, location))
    connection.commit()
    cursor.close()
def view_farmers():
    cursor = connection.cursor()
    query = "SELECT * FROM Farmer"
    cursor.execute(query)
    farmers = cursor.fetchall()
    cursor.close()
    return farmers
def update_farmer(farmer_id, name, phone, location):
    cursor = connection.cursor()
    query = """UPDATE Farmer SET farmer_name = %s,phone = %s,location = %s WHERE farmer_id = %s """
    cursor.execute(query, (name, phone, location, farmer_id))
    connection.commit()
    cursor.close()
def delete_farmer(farmer_id):
    cursor = connection.cursor()
    try:
        # Delete dependent rows first so the foreign keys remain enabled.
        cursor.execute("""
            DELETE cl
            FROM Crop_Loss AS cl
            INNER JOIN Cultivation AS cu
                ON cu.cultivation_id = cl.cultivation_id
            INNER JOIN Farm AS fm
                ON fm.farm_id = cu.farm_id
            WHERE fm.farmer_id = %s
        """, (farmer_id,))

        cursor.execute("""
            DELETE cu
            FROM Cultivation AS cu
            INNER JOIN Farm AS fm
                ON fm.farm_id = cu.farm_id
            WHERE fm.farmer_id = %s
        """, (farmer_id,))

        cursor.execute("DELETE FROM Farm WHERE farmer_id = %s", (farmer_id,))
        cursor.execute("DELETE FROM Farmer WHERE farmer_id = %s", (farmer_id,))
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
def add_farm(farmer_id, farm_name, location, area_acres):
    cursor = connection.cursor()
    query = """INSERT INTO Farm (farmer_id, farm_name, location, area_acres)VALUES (%s, %s, %s, %s)"""
    cursor.execute(query, (farmer_id, farm_name, location, area_acres))
    connection.commit()
    cursor.close()
def view_farms():
    cursor = connection.cursor()
    query = "SELECT * FROM Farm"
    cursor.execute(query)
    farms = cursor.fetchall()
    cursor.close()
    return farms
def update_farm(farm_id, farmer_id, farm_name, location, area_acres):
    cursor = connection.cursor()
    query = """UPDATE Farm SET farmer_id = %s,farm_name = %s,location = %s,area_acres = %s WHERE farm_id = %s"""
    cursor.execute(query,(farmer_id, farm_name, location, area_acres, farm_id))
    connection.commit()
    cursor.close()
def delete_farm(farm_id):
    cursor = connection.cursor()
    query = """DELETE FROM Farm WHERE farm_id = %s"""
    cursor.execute(query, (farm_id,))
    connection.commit()
    cursor.close()
def add_crop(crop_name, crop_type, season):
    cursor = connection.cursor()
    query = """INSERT INTO Crop (crop_name, crop_type, season)VALUES (%s, %s, %s)"""
    cursor.execute(query, (crop_name, crop_type, season))
    connection.commit()
    cursor.close()
def view_crops():
    cursor = connection.cursor()
    query = "SELECT * FROM Crop"
    cursor.execute(query)
    crops = cursor.fetchall()
    cursor.close()
    return crops
def update_crop(crop_id, crop_name, crop_type, season):
    cursor = connection.cursor()
    query = """UPDATE Crop SET crop_name = %s,crop_type = %s,season = %s WHERE crop_id = %s"""
    cursor.execute(query,(crop_name, crop_type, season, crop_id))
    connection.commit()
    cursor.close()
def delete_crop(crop_id):
    cursor = connection.cursor()
    query = """DELETE FROM Crop WHERE crop_id = %s"""
    cursor.execute(query, (crop_id,))
    connection.commit()
    cursor.close()
def add_cultivation(farm_id, crop_id, sowing_date, harvest_date, expected_yield, actual_yield):
    cursor = connection.cursor()
    query = """INSERT INTO Cultivation(farm_id, crop_id, sowing_date, harvest_date, expected_yield, actual_yield)VALUES (%s, %s, %s, %s, %s, %s)"""
    cursor.execute(query,(farm_id, crop_id, sowing_date, harvest_date, expected_yield, actual_yield))
    connection.commit()
    cursor.close()
def view_cultivations():
    cursor = connection.cursor()
    query = """SELECT cultivation_id, farm_id, crop_id, sowing_date, harvest_date, expected_yield, actual_yield FROM Cultivation"""
    cursor.execute(query)
    cultivations = cursor.fetchall()
    cursor.close()
    return cultivations
def update_cultivation(cultivation_id, farm_id, crop_id, sowing_date, harvest_date, expected_yield, actual_yield):
    cursor = connection.cursor()
    query = """UPDATE Cultivation SET farm_id = %s,crop_id = %s,sowing_date = %s,harvest_date = %s,expected_yield = %s,actual_yield = %s WHERE cultivation_id = %s"""
    cursor.execute(query,(farm_id, crop_id, sowing_date, harvest_date,expected_yield, actual_yield, cultivation_id))
    connection.commit()
    cursor.close()
def delete_cultivation(cultivation_id):
    cursor = connection.cursor()
    query = """DELETE FROM Cultivation WHERE cultivation_id = %s"""
    cursor.execute(query, (cultivation_id,))
    connection.commit()
    cursor.close()
def add_loss_reason(reason_name, description):
    cursor = connection.cursor()
    query = """INSERT INTO Loss_Reason (reason_name, description) VALUES (%s, %s)"""
    cursor.execute(query, (reason_name, description))
    connection.commit()
    cursor.close()
def view_loss_reasons():
    cursor = connection.cursor()
    query = "SELECT * FROM Loss_Reason"
    cursor.execute(query)
    reasons = cursor.fetchall()
    cursor.close()
    return reasons
def update_loss_reason(reason_id, reason_name, description):
    cursor = connection.cursor()
    query = """UPDATE Loss_Reason SET reason_name = %s,description = %s WHERE reason_id = %s"""
    cursor.execute(query,(reason_name, description, reason_id))
    connection.commit()
    cursor.close()
def delete_loss_reason(reason_id):
    cursor = connection.cursor()
    query = """DELETE FROM Loss_Reason WHERE reason_id = %s"""
    cursor.execute(query, (reason_id,))
    connection.commit()
    cursor.close()
def add_prevention_measure(reason_id, prevention_action):
    cursor = connection.cursor()
    query = """INSERT INTO Prevention_Measure (reason_id, prevention_action) VALUES (%s, %s)"""
    cursor.execute(query,(reason_id, prevention_action))
    connection.commit()
    cursor.close()
def view_prevention_measures():
    cursor = connection.cursor()
    query = "SELECT * FROM Prevention_Measure"
    cursor.execute(query)
    measures = cursor.fetchall()
    cursor.close()
    return measures
def update_prevention_measure(prevention_id, reason_id, prevention_action):
    cursor = connection.cursor()
    query = """UPDATE Prevention_Measure SET reason_id = %s,prevention_action = %s WHERE prevention_id = %s"""
    cursor.execute(query,(reason_id, prevention_action, prevention_id))
    connection.commit()
    cursor.close()
def delete_prevention_measure(prevention_id):
    cursor = connection.cursor()
    query = """DELETE FROM Prevention_Measure WHERE prevention_id = %s"""
    cursor.execute(query, (prevention_id,))
    connection.commit()
    cursor.close()
def add_crop_loss(cultivation_id, loss_date, loss_quantity, loss_percentage, reason_id):
    cursor = connection.cursor()
    query = """INSERT INTO Crop_Loss(cultivation_id, loss_date, loss_quantity, loss_percentage, reason_id)VALUES (%s, %s, %s, %s, %s)"""
    cursor.execute(query,(cultivation_id, loss_date, loss_quantity, loss_percentage, reason_id))
    connection.commit()
    cursor.close()
def view_crop_losses():
    cursor = connection.cursor()
    query = "SELECT * FROM Crop_Loss"
    cursor.execute(query)
    losses = cursor.fetchall()
    cursor.close()
    return losses
def update_crop_loss(loss_id, cultivation_id, loss_date, loss_quantity, loss_percentage, reason_id):
    cursor = connection.cursor()
    query = """UPDATE Crop_Loss SET cultivation_id = %s,loss_date = %s,loss_quantity = %s,loss_percentage = %s,reason_id = %s WHERE loss_id = %s"""
    cursor.execute(query,(cultivation_id, loss_date, loss_quantity,loss_percentage, reason_id, loss_id))
    connection.commit()
    cursor.close()
def delete_crop_loss(loss_id):
    cursor = connection.cursor()
    query = """DELETE FROM Crop_Loss WHERE loss_id = %s"""
    cursor.execute(query, (loss_id,))
    connection.commit()
    cursor.close()
# =========================
# FRONTEND START
# =========================
# =========================================================
# FARMER MANAGEMENT WINDOW
# =========================================================
def open_farmer_window(parent):
    farmer_window = tk.Frame(parent, bg="#F4F1E6")
    farmer_window.pack(fill="both", expand=True)
    header = tk.Frame(farmer_window,bg="#1B5E20",height=85)
    header.pack(fill="x")
    header.pack_propagate(False)
    tk.Label(header,text="FARMER MANAGEMENT",font=("Arial", 22, "bold"),bg="#1B5E20",fg="white").pack(pady=(15, 2))
    tk.Label(header,text="Manage farmer information",font=("Arial", 10),bg="#1B5E20",fg="#DDEED8").pack()
# =====================================================
# FORM CARD
# =====================================================
    form_card = tk.Frame(farmer_window,bg="#FFFDF5",bd=1,relief="solid")
    form_card.pack(fill="x",padx=35,pady=25)
    tk.Label(form_card,text="Farmer Details",font=("Arial", 15, "bold"),bg="#FFFDF5",fg="#1B5E20").grid(row=0,column=0,columnspan=4,sticky="w",padx=25,pady=(18, 15))
# Farmer ID
    tk.Label(form_card,text="Farmer ID",font=("Arial", 10, "bold"),bg="#FFFDF5",fg="#4E4E35").grid(row=1,column=0,padx=(25, 10),pady=10,sticky="w")
    farmer_id_entry = tk.Entry(form_card,width=25,font=("Arial", 11),relief="solid",bd=1)
    farmer_id_entry.grid(row=1,column=1,padx=10,pady=10 )
    tk.Label(form_card,text="Farmer Name",font=("Arial", 10, "bold"),bg="#FFFDF5",fg="#4E4E35").grid(row=1,column=2,padx=(35, 10),pady=10,sticky="w")
    farmer_name_entry = tk.Entry(form_card,width=25,font=("Arial", 11),relief="solid",bd=1)
    farmer_name_entry.grid(row=1,column=3,padx=(10, 25),pady=10)
    tk.Label(form_card,text="Phone",font=("Arial", 10, "bold"),bg="#FFFDF5",fg="#4E4E35").grid(row=2,column=0,padx=(25, 10),pady=10,sticky="w")
    phone_entry = tk.Entry(form_card,width=25,font=("Arial", 11),relief="solid",bd=1)
    phone_entry.grid(row=2,column=1,padx=10,pady=10)
# Location
    tk.Label(form_card,text="Location",font=("Arial", 10, "bold"),bg="#FFFDF5",fg="#4E4E35").grid(row=2,column=2,padx=(35, 10),pady=10,sticky="w")
    location_entry = tk.Entry(form_card,width=25,font=("Arial", 11),relief="solid",bd=1)
    location_entry.grid(row=2,column=3,padx=(10, 25),pady=10)

    def clear_fields():

        farmer_id_entry.delete(0, tk.END)
        farmer_name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        location_entry.delete(0, tk.END)

    def refresh_table():

        for item in farmer_table.get_children():
            farmer_table.delete(item)

        try:
            farmers = view_farmers()

            for farmer in farmers:
                farmer_table.insert(
                    "",
                    tk.END,
                    values=farmer
                )

        except mysql.connector.Error as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    def add_farmer_data():

        name = farmer_name_entry.get().strip()
        phone = phone_entry.get().strip()
        location = location_entry.get().strip()

        if name == "" or phone == "" or location == "":
            messagebox.showwarning(
                "Missing Information",
                "Please enter Farmer Name, Phone and Location."
            )
            return
        if not phone.isdigit():
            messagebox.showwarning(
                "Invalid Phone",
                "Phone number must contain digits only."
            )
            return

        if len(phone) != 10:
            messagebox.showwarning(
                "Invalid Phone",
                "Phone number must contain exactly 10 digits."
            )
            return
        try:

            add_farmer(
                name,
                phone,
                location
            )

            messagebox.showinfo(
                "Success",
                "Farmer added successfully."
            )

            clear_fields()
            refresh_table()

        except mysql.connector.Error as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    def update_farmer_data():

        farmer_id = farmer_id_entry.get().strip()
        name = farmer_name_entry.get().strip()
        phone = phone_entry.get().strip()
        location = location_entry.get().strip()

        if (
                farmer_id == ""
                or name == ""
                or phone == ""
                or location == ""
        ):
            messagebox.showwarning(
                "Missing Information",
                "Please select a farmer and fill all fields."
            )
            return

        try:

            update_farmer(
                farmer_id,
                name,
                phone,
                location
            )

            messagebox.showinfo(
                "Success",
                "Farmer updated successfully."
            )

            clear_fields()
            refresh_table()

        except mysql.connector.Error as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    def delete_farmer_data():

        farmer_id = farmer_id_entry.get().strip()

        if farmer_id == "":
            messagebox.showwarning(
                "Missing Farmer ID",
                "Please select a farmer to delete."
            )
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this farmer?"
        )

        if not confirm:
            return

        try:

            delete_farmer(farmer_id)

            messagebox.showinfo(
                "Success",
                "Farmer deleted successfully."
            )

            clear_fields()
            refresh_table()

        except mysql.connector.Error as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    # =====================================================
    # BUTTONS
    # =====================================================

    button_frame = tk.Frame(
        farmer_window,
        bg="#F4F1E6"
    )
    button_frame.pack(
        fill="x",
        padx=35,
        pady=(0, 20)
    )

    tk.Button(
        button_frame,
        text="ADD FARMER",
        font=("Arial", 10, "bold"),
        bg="#2E7D32",
        fg="white",
        activebackground="#1B5E20",
        activeforeground="white",
        width=16,
        height=2,
        relief="flat",
        cursor="hand2",
        command=add_farmer_data
    ).pack(
        side="left",
        padx=5
    )

    tk.Button(
        button_frame,
        text="UPDATE",
        font=("Arial", 10, "bold"),
        bg="#558B2F",
        fg="white",
        activebackground="#33691E",
        activeforeground="white",
        width=16,
        height=2,
        relief="flat",
        cursor="hand2",
        command=update_farmer_data
    ).pack(
        side="left",
        padx=5
    )

    tk.Button(
        button_frame,
        text="DELETE",
        font=("Arial", 10, "bold"),
        bg="#8D4A3A",
        fg="white",
        activebackground="#6D3025",
        activeforeground="white",
        width=16,
        height=2,
        relief="flat",
        cursor="hand2",
        command=delete_farmer_data
    ).pack(
        side="left",
        padx=5
    )

    tk.Button(
        button_frame,
        text="CLEAR",
        font=("Arial", 10, "bold"),
        bg="#8A7654",
        fg="white",
        activebackground="#6E5D42",
        activeforeground="white",
        width=16,
        height=2,
        relief="flat",
        cursor="hand2",
        command=clear_fields
    ).pack(
        side="left",
        padx=5
    )

    # =====================================================
    # TABLE CARD
    # =====================================================

    table_card = tk.Frame(
        farmer_window,
        bg="#FFFDF5",
        bd=1,
        relief="solid"
    )
    table_card.pack(
        fill="both",
        expand=True,
        padx=35,
        pady=(0, 30)
    )

    tk.Label(
        table_card,
        text="Registered Farmers",
        font=("Arial", 14, "bold"),
        bg="#FFFDF5",
        fg="#1B5E20"
    ).pack(
        anchor="w",
        padx=20,
        pady=(15, 10)
    )

    table_container = tk.Frame(
        table_card,
        bg="#FFFDF5"
    )
    table_container.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=(0, 20)
    )

    columns = (
        "Farmer ID",
        "Farmer Name",
        "Phone",
        "Location"
    )

    farmer_table = ttk.Treeview(
        table_container,
        columns=columns,
        show="headings",
        height=10
    )

    farmer_table.heading(
        "Farmer ID",
        text="ID"
    )

    farmer_table.heading(
        "Farmer Name",
        text="Farmer Name"
    )

    farmer_table.heading(
        "Phone",
        text="Phone"
    )

    farmer_table.heading(
        "Location",
        text="Location"
    )

    farmer_table.column(
        "Farmer ID",
        width=100,
        anchor="center"
    )

    farmer_table.column(
        "Farmer Name",
        width=250,
        anchor="center"
    )

    farmer_table.column(
        "Phone",
        width=200,
        anchor="center"
    )

    farmer_table.column(
        "Location",
        width=250,
        anchor="center"
    )

    farmer_table.pack(
        fill="both",
        expand=True
    )
# =====================================================
    # SELECT TABLE ROW
    # =====================================================

    def select_farmer(event):

        selected_item = farmer_table.focus()

        if selected_item == "":
            return

        values = farmer_table.item(
            selected_item,
            "values"
        )

        clear_fields()

        farmer_id_entry.insert(
            0,
            values[0]
        )

        farmer_name_entry.insert(
            0,
            values[1]
        )

        phone_entry.insert(
            0,
            values[2]
        )

        location_entry.insert(
            0,
            values[3]
        )

    farmer_table.bind(
        "<ButtonRelease-1>",
        select_farmer
    )

    # Load existing farmers

    refresh_table()
# =========================================================
# FARM MANAGEMENT WINDOW
# =========================================================

def open_farm_window(parent):

    farm_window = tk.Frame(parent)
    farm_window.pack(fill="both", expand=True)
    farm_window.configure(bg="#F4F1E6")

    # =====================================================
    # HEADER
    # =====================================================

    header = tk.Frame(
        farm_window,
        bg="#1B5E20",
        height=85
    )
    header.pack(fill="x")
    header.pack_propagate(False)

    tk.Label(
        header,
        text="FARM MANAGEMENT",
        font=("Arial", 22, "bold"),
        bg="#1B5E20",
        fg="white"
    ).pack(pady=(15, 2))

    tk.Label(
        header,
        text="Manage farm and land information",
        font=("Arial", 10),
        bg="#1B5E20",
        fg="#DDEED8"
    ).pack()

    # =====================================================
    # FORM CARD
    # =====================================================

    form_card = tk.Frame(
        farm_window,
        bg="#FFFDF5",
        bd=1,
        relief="solid"
    )
    form_card.pack(
        fill="x",
        padx=35,
        pady=25
    )

    tk.Label(
        form_card,
        text="Farm Details",
        font=("Arial", 15, "bold"),
        bg="#FFFDF5",
        fg="#1B5E20"
    ).grid(
        row=0,
        column=0,
        columnspan=4,
        sticky="w",
        padx=25,
        pady=(18, 15)
    )

    # =====================================================
    # FARM ID
    # =====================================================

    tk.Label(
        form_card,
        text="Farm ID",
        font=("Arial", 10, "bold"),
        bg="#FFFDF5",
        fg="#4E4E35"
    ).grid(
        row=1,
        column=0,
        padx=(25, 10),
        pady=10,
        sticky="w"
    )

    farm_id_entry = tk.Entry(
        form_card,
        width=25,
        font=("Arial", 11),
        relief="solid",
        bd=1
    )
    farm_id_entry.grid(
        row=1,
        column=1,
        padx=10,
        pady=10
    )

    # =====================================================
    # FARMER ID
    # =====================================================

    tk.Label(
        form_card,
        text="Farmer ID",
        font=("Arial", 10, "bold"),
        bg="#FFFDF5",
        fg="#4E4E35"
    ).grid(
        row=1,
        column=2,
        padx=(35, 10),
        pady=10,
        sticky="w"
    )

    farmer_id_entry = tk.Entry(
        form_card,
        width=25,
        font=("Arial", 11),
        relief="solid",
        bd=1
    )
    farmer_id_entry.grid(
        row=1,
        column=3,
        padx=(10, 25),
        pady=10
    )

    # =====================================================
    # FARM NAME
    # =====================================================

    tk.Label(
        form_card,
        text="Farm Name",
        font=("Arial", 10, "bold"),
        bg="#FFFDF5",
        fg="#4E4E35"
    ).grid(
        row=2,
        column=0,
        padx=(25, 10),
        pady=10,
        sticky="w"
    )

    farm_name_entry = tk.Entry(
        form_card,
        width=25,
        font=("Arial", 11),
        relief="solid",
        bd=1
    )
    farm_name_entry.grid(
        row=2,
        column=1,
        padx=10,
        pady=10
    )

    # =====================================================
    # LOCATION
    # =====================================================

    tk.Label(
        form_card,
        text="Location",
        font=("Arial", 10, "bold"),
        bg="#FFFDF5",
        fg="#4E4E35"
    ).grid(
        row=2,
        column=2,
        padx=(35, 10),
        pady=10,
        sticky="w"
    )

    location_entry = tk.Entry(
        form_card,
        width=25,
        font=("Arial", 11),
        relief="solid",
        bd=1
    )
    location_entry.grid(
        row=2,
        column=3,
        padx=(10, 25),
        pady=10
    )

    # =====================================================
    # AREA
    # =====================================================

    tk.Label(
        form_card,
        text="Area (Acres)",
        font=("Arial", 10, "bold"),
        bg="#FFFDF5",
        fg="#4E4E35"
    ).grid(
        row=3,
        column=0,
        padx=(25, 10),
        pady=10,
        sticky="w"
    )

    area_entry = tk.Entry(
        form_card,
        width=25,
        font=("Arial", 11),
        relief="solid",
        bd=1
    )
    area_entry.grid(
        row=3,
        column=1,
        padx=10,
        pady=10
    )
# =====================================================
    # FUNCTIONS
    # =====================================================
    def clear_fields():
        farm_id_entry.delete(0, tk.END)
        farmer_id_entry.delete(0, tk.END)
        farm_name_entry.delete(0, tk.END)
        location_entry.delete(0, tk.END)
        area_entry.delete(0, tk.END)
    def refresh_table():
        for item in farm_table.get_children():
            farm_table.delete(item)

        try:

            farms = view_farms()

            for farm in farms:
                farm_table.insert("",tk.END, values=farm)

        except mysql.connector.Error as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    def add_farm_data():

        farmer_id = farmer_id_entry.get().strip()
        farm_name = farm_name_entry.get().strip()
        location = location_entry.get().strip()
        area = area_entry.get().strip()

        if (
            farmer_id == ""
            or farm_name == ""
            or location == ""
            or area == ""
        ):
            messagebox.showwarning(
                "Missing Information",
                "Please fill all farm details."
            )
            return
        if not farmer_id.isdigit():
            messagebox.showwarning(
                "Invalid Farmer ID",
                "Farmer ID must contain digits only."
            )
            return

        try:
            float(area)
        except ValueError:
            messagebox.showwarning(
                "Invalid Area",
                "Area must be a valid number."
            )
            return

        try:

            farmer_id = int(farmer_id)
            area = float(area)

            add_farm(
                farmer_id,
                farm_name,
                location,
                area
            )

            messagebox.showinfo(
                "Success",
                "Farm added successfully."
            )

            clear_fields()
            refresh_table()

        except ValueError:

            messagebox.showwarning(
                "Invalid Data",
                "Farmer ID must be a number and Area must be numeric."
            )

        except mysql.connector.Error as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    def update_farm_data():

        farm_id = farm_id_entry.get().strip()
        farmer_id = farmer_id_entry.get().strip()
        farm_name = farm_name_entry.get().strip()
        location = location_entry.get().strip()
        area = area_entry.get().strip()

        if (
            farm_id == ""
            or farmer_id == ""
            or farm_name == ""
            or location == ""
            or area == ""
        ):
            messagebox.showwarning(
                "Missing Information",
                "Please select a farm and fill all fields."
            )
            return

        try:

            farm_id = int(farm_id)
            farmer_id = int(farmer_id)
            area = float(area)

            update_farm(
                farm_id,
                farmer_id,
                farm_name,
                location,
                area
            )

            messagebox.showinfo(
                "Success",
                "Farm updated successfully."
            )

            clear_fields()
            refresh_table()

        except ValueError:

            messagebox.showwarning(
                "Invalid Data",
                "ID values must be numbers and Area must be numeric."
            )

        except mysql.connector.Error as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    def delete_farm_data():

        farm_id = farm_id_entry.get().strip()

        if farm_id == "":
            messagebox.showwarning(
                "Missing Farm ID",
                "Please select a farm to delete."
            )
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this farm?"
        )

        if not confirm:
            return

        try:

            farm_id = int(farm_id)

            delete_farm(farm_id)

            messagebox.showinfo(
                "Success",
                "Farm deleted successfully."
            )

            clear_fields()
            refresh_table()

        except ValueError:

            messagebox.showwarning(
                "Invalid Data",
                "Farm ID must be a number."
            )

        except mysql.connector.Error as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )
# =====================================================
    # BUTTONS
    # =====================================================

    button_frame = tk.Frame(
        farm_window,
        bg="#F4F1E6"
    )
    button_frame.pack(
        fill="x",
        padx=35,
        pady=(0, 20)
    )

    tk.Button(
        button_frame,
        text="ADD FARM",
        font=("Arial", 10, "bold"),
        bg="#2E7D32",
        fg="white",
        activebackground="#1B5E20",
        activeforeground="white",
        width=16,
        height=2,
        relief="flat",
        cursor="hand2",
        command=add_farm_data
    ).pack(
        side="left",
        padx=5
    )

    tk.Button(
        button_frame,
        text="UPDATE",
        font=("Arial", 10, "bold"),
        bg="#558B2F",
        fg="white",
        activebackground="#33691E",
        activeforeground="white",
        width=16,
        height=2,
        relief="flat",
        cursor="hand2",
        command=update_farm_data
    ).pack(
        side="left",
        padx=5
    )

    tk.Button(
        button_frame,
        text="DELETE",
        font=("Arial", 10, "bold"),
        bg="#8D4A3A",
        fg="white",
        activebackground="#6D3025",
        activeforeground="white",
        width=16,
        height=2,
        relief="flat",
        cursor="hand2",
        command=delete_farm_data
    ).pack(
        side="left",
        padx=5
    )

    tk.Button(
        button_frame,
        text="CLEAR",
        font=("Arial", 10, "bold"),
        bg="#8A7654",
        fg="white",
        activebackground="#6E5D42",
        activeforeground="white",
        width=16,
        height=2,
        relief="flat",
        cursor="hand2",
        command=clear_fields
    ).pack(
        side="left",
        padx=5
    )

    # =====================================================
    # TABLE CARD
    # =====================================================

    table_card = tk.Frame(
        farm_window,
        bg="#FFFDF5",
        bd=1,
        relief="solid"
    )
    table_card.pack(
        fill="both",
        expand=True,
        padx=35,
        pady=(0, 30)
    )

    tk.Label(
        table_card,
        text="Registered Farms",
        font=("Arial", 14, "bold"),
        bg="#FFFDF5",
        fg="#1B5E20"
    ).pack(
        anchor="w",
        padx=20,
        pady=(15, 10)
    )

    table_container = tk.Frame(
        table_card,
        bg="#FFFDF5"
    )
    table_container.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=(0, 20)
    )

    columns = (
        "Farm ID",
        "Farmer ID",
        "Farm Name",
        "Location",
        "Area"
    )

    farm_table = ttk.Treeview(
        table_container,
        columns=columns,
        show="headings",
        height=8
    )

    farm_table.heading(
        "Farm ID",
        text="Farm ID"
    )

    farm_table.heading(
        "Farmer ID",
        text="Farmer ID"
    )

    farm_table.heading(
        "Farm Name",
        text="Farm Name"
    )

    farm_table.heading(
        "Location",
        text="Location"
    )

    farm_table.heading(
        "Area",
        text="Area (Acres)"
    )

    farm_table.column(
        "Farm ID",
        width=100,
        anchor="center"
    )

    farm_table.column(
        "Farmer ID",
        width=110,
        anchor="center"
    )

    farm_table.column(
        "Farm Name",
        width=220,
        anchor="center"
    )

    farm_table.column(
        "Location",
        width=200,
        anchor="center"
    )

    farm_table.column(
        "Area",
        width=140,
        anchor="center"
    )

    farm_table.pack(
        fill="both",
        expand=True
    )

    # =====================================================
    # SELECT TABLE ROW
    # =====================================================

    def select_farm(event):

        selected_item = farm_table.focus()

        if selected_item == "":
            return

        values = farm_table.item(
            selected_item,
            "values"
        )

        clear_fields()

        farm_id_entry.insert(
            0,
            values[0]
        )

        farmer_id_entry.insert(
            0,
            values[1]
        )

        farm_name_entry.insert(
            0,
            values[2]
        )

        location_entry.insert(
            0,
            values[3]
        )

        area_entry.insert(
            0,
            values[4]
        )

    farm_table.bind(
        "<ButtonRelease-1>",
        select_farm
    )

    # Load existing farms

    refresh_table()

#=========================================
# CROP MANAGEMENT
#=========================================

def open_crop_window(parent):

    crop_window = tk.Frame(parent)
    crop_window.pack(fill="both", expand=True)
    crop_window.configure(bg="#F4F7F2")

    #-----------------------------------------
    # HEADER
    #-----------------------------------------

    header = tk.Frame(
        crop_window,
        bg="#1B5E20",
        height=80
    )
    header.pack(fill="x")
    header.pack_propagate(False)

    tk.Label(
        header,
        text="🌱 CROP MANAGEMENT",
        font=("Arial", 20, "bold"),
        bg="#1B5E20",
        fg="white"
    ).pack(anchor="w", padx=30, pady=(15, 0))

    tk.Label(
        header,
        text="Manage crops, crop types and cultivation seasons",
        font=("Arial", 10),
        bg="#1B5E20",
        fg="#DCEFD8"
    ).pack(anchor="w", padx=32, pady=2)

    #-----------------------------------------
    # SUMMARY CARDS
    #-----------------------------------------

    summary_frame = tk.Frame(
        crop_window,
        bg="#F4F7F2"
    )
    summary_frame.pack(fill="x", padx=25, pady=18)

    total_card = tk.Frame(
        summary_frame,
        bg="white",
        bd=1,
        relief="solid"
    )
    total_card.pack(
        side="left",
        fill="both",
        expand=True,
        padx=7
    )

    tk.Label(
        total_card,
        text="TOTAL CROPS",
        font=("Arial", 10, "bold"),
        bg="white",
        fg="#666666"
    ).pack(pady=(12, 2))

    total_label = tk.Label(
        total_card,
        text="0",
        font=("Arial", 22, "bold"),
        bg="white",
        fg="#1B5E20"
    )
    total_label.pack(pady=(0, 12))

    type_card = tk.Frame(
        summary_frame,
        bg="white",
        bd=1,
        relief="solid"
    )
    type_card.pack(
        side="left",
        fill="both",
        expand=True,
        padx=7
    )

    tk.Label(
        type_card,
        text="CROP TYPES",
        font=("Arial", 10, "bold"),
        bg="white",
        fg="#666666"
    ).pack(pady=(12, 2))

    type_label = tk.Label(
        type_card,
        text="0",
        font=("Arial", 22, "bold"),
        bg="white",
        fg="#558B2F"
    )
    type_label.pack(pady=(0, 12))

    season_card = tk.Frame(
        summary_frame,
        bg="white",
        bd=1,
        relief="solid"
    )
    season_card.pack(
        side="left",
        fill="both",
        expand=True,
        padx=7
    )

    tk.Label(
        season_card,
        text="SEASONS",
        font=("Arial", 10, "bold"),
        bg="white",
        fg="#666666"
    ).pack(pady=(12, 2))

    season_label = tk.Label(
        season_card,
        text="0",
        font=("Arial", 22, "bold"),
        bg="white",
        fg="#33691E"
    )
    season_label.pack(pady=(0, 12))

    #-----------------------------------------
    # SEARCH + FILTER
    #-----------------------------------------

    filter_frame = tk.Frame(
        crop_window,
        bg="#E8F5E9",
        bd=1,
        relief="solid"
    )
    filter_frame.pack(
        fill="x",
        padx=32,
        pady=(0, 15)
    )

    tk.Label(
        filter_frame,
        text="Search Crop:",
        font=("Arial", 10, "bold"),
        bg="#E8F5E9"
    ).grid(
        row=0,
        column=0,
        padx=(15, 5),
        pady=12
    )

    search_entry = tk.Entry(
        filter_frame,
        font=("Arial", 10),
        width=25
    )
    search_entry.grid(
        row=0,
        column=1,
        padx=5,
        pady=12
    )

    tk.Label(
        filter_frame,
        text="Crop Type:",
        font=("Arial", 10, "bold"),
        bg="#E8F5E9"
    ).grid(
        row=0,
        column=2,
        padx=(20, 5),
        pady=12
    )

    type_combo = ttk.Combobox(
        filter_frame,
        width=15,
        state="readonly"
    )
    type_combo.grid(
        row=0,
        column=3,
        padx=5,
        pady=12
    )

    tk.Label(
        filter_frame,
        text="Season:",
        font=("Arial", 10, "bold"),
        bg="#E8F5E9"
    ).grid(
        row=0,
        column=4,
        padx=(20, 5),
        pady=12
    )

    season_combo = ttk.Combobox(
        filter_frame,
        width=15,
        state="readonly"
    )
    season_combo.grid(
        row=0,
        column=5,
        padx=5,
        pady=12
    )

    #-----------------------------------------
    # FORM
    #-----------------------------------------

    form_card = tk.Frame(
        crop_window,
        bg="#FFFDF5",
        bd=1,
        relief="solid"
    )
    form_card.pack(
        fill="x",
        padx=32,
        pady=(0, 15)
    )

    tk.Label(
        form_card,
        text="Crop Information",
        font=("Arial", 12, "bold"),
        bg="#FFFDF5",
        fg="#1B5E20"
    ).grid(
        row=0,
        column=0,
        columnspan=6,
        sticky="w",
        padx=20,
        pady=(12, 10)
    )

    tk.Label(
        form_card,
        text="Crop ID",
        bg="#FFFDF5",
        font=("Arial", 10, "bold")
    ).grid(row=1, column=0, padx=10, pady=8)

    crop_id_entry = tk.Entry(
        form_card,
        width=15,
        font=("Arial", 10)
    )
    crop_id_entry.grid(row=1, column=1, padx=10, pady=8)

    tk.Label(
        form_card,
        text="Crop Name",
        bg="#FFFDF5",
        font=("Arial", 10, "bold")
    ).grid(row=1, column=2, padx=10, pady=8)

    crop_name_entry = tk.Entry(
        form_card,
        width=18,
        font=("Arial", 10)
    )
    crop_name_entry.grid(row=1, column=3, padx=10, pady=8)

    tk.Label(
        form_card,
        text="Crop Type",
        bg="#FFFDF5",
        font=("Arial", 10, "bold")
    ).grid(row=1, column=4, padx=10, pady=8)

    crop_type_entry = tk.Entry(
        form_card,
        width=18,
        font=("Arial", 10)
    )
    crop_type_entry.grid(row=1, column=5, padx=10, pady=8)

    tk.Label(
        form_card,
        text="Season",
        bg="#FFFDF5",
        font=("Arial", 10, "bold")
    ).grid(row=2, column=0, padx=10, pady=8)

    season_entry = tk.Entry(
        form_card,
        width=15,
        font=("Arial", 10)
    )
    season_entry.grid(row=2, column=1, padx=10, pady=8)

    #-----------------------------------------
    # FUNCTIONS
    #-----------------------------------------

    def clear_fields():
        crop_id_entry.delete(0, tk.END)
        crop_name_entry.delete(0, tk.END)
        crop_type_entry.delete(0, tk.END)
        season_entry.delete(0, tk.END)

    def load_crops():

        for item in crop_table.get_children():
            crop_table.delete(item)

        crops = view_crops()

        search_text = search_entry.get().lower()
        selected_type = type_combo.get()
        selected_season = season_combo.get()

        filtered_crops = []

        for crop in crops:

            crop_id = str(crop[0])
            crop_name = str(crop[1])
            crop_type = str(crop[2])
            season = str(crop[3])

            if search_text not in crop_name.lower():
                continue

            if selected_type != "All" and crop_type != selected_type:
                continue

            if selected_season != "All" and season != selected_season:
                continue

            filtered_crops.append(crop)

            crop_table.insert(
                "",
                tk.END,
                values=crop
            )

        # Update summary
        total_label.config(
            text=str(len(filtered_crops))
        )

        types = set()

        for crop in filtered_crops:
            types.add(crop[2])

        type_label.config(
            text=str(len(types))
        )

        seasons = set()

        for crop in filtered_crops:
            seasons.add(crop[3])

        season_label.config(
            text=str(len(seasons))

        )

    def refresh_filters():

        crops = view_crops()

        types = sorted(
            set(crop[2] for crop in crops)
        )

        seasons = sorted(
            set(crop[3] for crop in crops)
        )

        type_combo["values"] = ["All"] + types
        season_combo["values"] = ["All"] + seasons

        if type_combo.get() == "":
            type_combo.set("All")

        if season_combo.get() == "":
            season_combo.set("All")

        load_crops()

    def add_crop_data():

        name = crop_name_entry.get().strip()
        crop_type = crop_type_entry.get().strip()
        season = season_entry.get().strip()

        if name == "" or crop_type == "" or season == "":
            messagebox.showwarning(
                "Missing Information",
                "Please fill all crop details."
            )
            return

        try:
            add_crop(
                name,
                crop_type,
                season
            )

            messagebox.showinfo(
                "Success",
                "Crop added successfully!"
            )

            clear_fields()
            refresh_filters()

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e)
            )

    def update_crop_data():

        crop_id = crop_id_entry.get().strip()
        name = crop_name_entry.get().strip()
        crop_type = crop_type_entry.get().strip()
        season = season_entry.get().strip()

        if crop_id == "":
            messagebox.showwarning(
                "Select Crop",
                "Please select a crop from the table."
            )
            return

        if name == "" or crop_type == "" or season == "":
            messagebox.showwarning(
                "Missing Information",
                "Please fill all crop details."
            )
            return

        try:
            update_crop(
                crop_id,
                name,
                crop_type,
                season
            )

            messagebox.showinfo(
                "Success",
                "Crop updated successfully!"
            )

            clear_fields()
            refresh_filters()

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e)
            )

    def delete_crop_data():

        crop_id = crop_id_entry.get().strip()

        if crop_id == "":
            messagebox.showwarning(
                "Select Crop",
                "Please select a crop from the table."
            )
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this crop?"
        )

        if confirm:

            try:
                delete_crop(crop_id)

                messagebox.showinfo(
                    "Deleted",
                    "Crop deleted successfully!"
                )

                clear_fields()
                refresh_filters()

            except Exception as e:
                messagebox.showerror(
                    "Error",
                    "This crop may be used in cultivation records.\n\n"
                    + str(e)
                )

    def select_crop(event):

        selected = crop_table.selection()

        if not selected:
            return

        values = crop_table.item(
            selected[0],
            "values"
        )

        clear_fields()

        crop_id_entry.insert(
            0,
            values[0]
        )

        crop_name_entry.insert(
            0,
            values[1]
        )

        crop_type_entry.insert(
            0,
            values[2]
        )

        season_entry.insert(
            0,
            values[3]
        )

    #-----------------------------------------
    # BUTTONS
    #-----------------------------------------

    button_frame = tk.Frame(
        form_card,
        bg="#FFFDF5"
    )
    button_frame.grid(
        row=2,
        column=2,
        columnspan=4,
        padx=10,
        pady=10
    )

    tk.Button(
        button_frame,
        text="➕ ADD CROP",
        font=("Arial", 9, "bold"),
        bg="#2E7D32",
        fg="white",
        width=13,
        relief="flat",
        cursor="hand2",
        command=add_crop_data
    ).pack(side="left", padx=5)

    tk.Button(
        button_frame,
        text="✏ UPDATE",
        font=("Arial", 9, "bold"),
        bg="#558B2F",
        fg="white",
        width=13,
        relief="flat",
        cursor="hand2",
        command=update_crop_data
    ).pack(side="left", padx=5)

    tk.Button(
        button_frame,
        text="🗑 DELETE",
        font=("Arial", 9, "bold"),
        bg="#C62828",
        fg="white",
        width=13,
        relief="flat",
        cursor="hand2",
        command=delete_crop_data
    ).pack(side="left", padx=5)

    tk.Button(
        button_frame,
        text="CLEAR",
        font=("Arial", 9, "bold"),
        bg="#757575",
        fg="white",
        width=13,
        relief="flat",
        cursor="hand2",
        command=clear_fields
    ).pack(side="left", padx=5)

    #-----------------------------------------
    # TABLE
    #-----------------------------------------

    table_frame = tk.Frame(
        crop_window,
        bg="white",
        bd=1,
        relief="solid"
    )
    table_frame.pack(
        fill="both",
        expand=True,
        padx=32,
        pady=(0, 25)
    )

    tk.Label(
        table_frame,
        text="Registered Crops",
        font=("Arial", 12, "bold"),
        bg="white",
        fg="#1B5E20"
    ).pack(
        anchor="w",
        padx=15,
        pady=10
    )

    tree_container = tk.Frame(
        table_frame,
        bg="white"
    )
    tree_container.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=(0, 15)
    )

    columns = (
        "Crop ID",
        "Crop Name",
        "Crop Type",
        "Season"
    )

    crop_table = ttk.Treeview(
        tree_container,
        columns=columns,
        show="headings",
        height=7
    )

    for column in columns:

        crop_table.heading(
            column,
            text=column
        )

        crop_table.column(
            column,
            width=180,
            anchor="center"
        )

    scrollbar = ttk.Scrollbar(
        tree_container,
        orient="vertical",
        command=crop_table.yview
    )

    crop_table.configure(
        yscrollcommand=scrollbar.set
    )

    crop_table.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )

    crop_table.bind(
        "<ButtonRelease-1>",
        select_crop
    )

    search_entry.bind(
        "<KeyRelease>",
        lambda event: load_crops()
    )

    type_combo.bind(
        "<<ComboboxSelected>>",
        lambda event: load_crops()
    )

    season_combo.bind(
        "<<ComboboxSelected>>",
        lambda event: load_crops()
    )

    #-----------------------------------------
    # LOAD DATA
    #-----------------------------------------

    refresh_filters()
#=========================================
# CULTIVATION MANAGEMENT
#=========================================

def open_cultivation_window(parent):

    cultivation_window = tk.Frame(parent)
    cultivation_window.pack(fill="both", expand=True)
    cultivation_window.configure(bg="#F4F7F2")

    #-----------------------------------------
    # HEADER
    #-----------------------------------------

    header = tk.Frame(
        cultivation_window,
        bg="#1B5E20",
        height=80
    )
    header.pack(fill="x")
    header.pack_propagate(False)

    tk.Label(
        header,
        text="🌾 CULTIVATION MANAGEMENT",
        font=("Arial", 20, "bold"),
        bg="#1B5E20",
        fg="white"
    ).pack(anchor="w", padx=30, pady=(15, 0))

    tk.Label(
        header,
        text="Track crop cultivation, harvesting and yield performance",
        font=("Arial", 10),
        bg="#1B5E20",
        fg="#DCEFD8"
    ).pack(anchor="w", padx=32, pady=2)
#-----------------------------------------
    # SUMMARY CARDS
    #-----------------------------------------

    summary_frame = tk.Frame(
        cultivation_window,
        bg="#F4F7F2"
    )
    summary_frame.pack(
        fill="x",
        padx=25,
        pady=18
    )

    card1 = tk.Frame(
        summary_frame,
        bg="white",
        bd=1,
        relief="solid"
    )
    card1.pack(
        side="left",
        fill="both",
        expand=True,
        padx=7
    )

    tk.Label(
        card1,
        text="TOTAL CULTIVATIONS",
        font=("Arial", 10, "bold"),
        bg="white",
        fg="#666666"
    ).pack(pady=(12, 2))

    total_label = tk.Label(
        card1,
        text="0",
        font=("Arial", 22, "bold"),
        bg="white",
        fg="#1B5E20"
    )
    total_label.pack(pady=(0, 12))

    card2 = tk.Frame(
        summary_frame,
        bg="white",
        bd=1,
        relief="solid"
    )
    card2.pack(
        side="left",
        fill="both",
        expand=True,
        padx=7
    )

    tk.Label(
        card2,
        text="COMPLETED HARVESTS",
        font=("Arial", 10, "bold"),
        bg="white",
        fg="#666666"
    ).pack(pady=(12, 2))

    harvest_label = tk.Label(
        card2,
        text="0",
        font=("Arial", 22, "bold"),
        bg="white",
        fg="#558B2F"
    )
    harvest_label.pack(pady=(0, 12))

    card3 = tk.Frame(
        summary_frame,
        bg="white",
        bd=1,
        relief="solid"
    )
    card3.pack(
        side="left",
        fill="both",
        expand=True,
        padx=7
    )

    tk.Label(
        card3,
        text="TOTAL EXPECTED YIELD (kg)",
        font=("Arial", 10, "bold"),
        bg="white",
        fg="#666666"
    ).pack(pady=(12, 2))

    expected_label = tk.Label(
        card3,
        text="0.00",
        font=("Arial", 20, "bold"),
        bg="white",
        fg="#33691E"
    )
    expected_label.pack(pady=(0, 12))

    card4 = tk.Frame(
        summary_frame,
        bg="white",
        bd=1,
        relief="solid"
    )
    card4.pack(
        side="left",
        fill="both",
        expand=True,
        padx=7
    )

    tk.Label(
        card4,
        text="TOTAL ACTUAL YIELD (kg)",
        font=("Arial", 10, "bold"),
        bg="white",
        fg="#666666"
    ).pack(pady=(12, 2))

    actual_label = tk.Label(
        card4,
        text="0.00",
        font=("Arial", 20, "bold"),
        bg="white",
        fg="#2E7D32"
    )
    actual_label.pack(pady=(0, 12))
#-----------------------------------------
    # FILTER SECTION
    #-----------------------------------------

    filter_frame = tk.Frame(
        cultivation_window,
        bg="#E8F5E9",
        bd=1,
        relief="solid"
    )
    filter_frame.pack(
        fill="x",
        padx=32,
        pady=(0, 15)
    )

    tk.Label(
        filter_frame,
        text="Search:",
        font=("Arial", 10, "bold"),
        bg="#E8F5E9"
    ).grid(
        row=0,
        column=0,
        padx=(15, 5),
        pady=12
    )

    search_entry = tk.Entry(
        filter_frame,
        width=22,
        font=("Arial", 10)
    )
    search_entry.grid(
        row=0,
        column=1,
        padx=5,
        pady=12
    )

    tk.Label(
        filter_frame,
        text="Farm:",
        font=("Arial", 10, "bold"),
        bg="#E8F5E9"
    ).grid(
        row=0,
        column=2,
        padx=(20, 5),
        pady=12
    )

    farm_filter = ttk.Combobox(
        filter_frame,
        width=18,
        state="readonly"
    )
    farm_filter.grid(
        row=0,
        column=3,
        padx=5,
        pady=12
    )

    tk.Label(
        filter_frame,
        text="Crop:",
        font=("Arial", 10, "bold"),
        bg="#E8F5E9"
    ).grid(
        row=0,
        column=4,
        padx=(20, 5),
        pady=12
    )

    crop_filter = ttk.Combobox(
        filter_frame,
        width=18,
        state="readonly"
    )
    crop_filter.grid(
        row=0,
        column=5,
        padx=5,
        pady=12
    )
#-----------------------------------------
    # FORM
    #-----------------------------------------

    form_card = tk.Frame(
        cultivation_window,
        bg="#FFFDF5",
        bd=1,
        relief="solid"
    )
    form_card.pack(
        fill="x",
        padx=32,
        pady=(0, 15)
    )

    tk.Label(
        form_card,
        text="Cultivation Information",
        font=("Arial", 12, "bold"),
        bg="#FFFDF5",
        fg="#1B5E20"
    ).grid(
        row=0,
        column=0,
        columnspan=8,
        sticky="w",
        padx=20,
        pady=(12, 10)
    )

    # Cultivation ID

    tk.Label(
        form_card,
        text="Cultivation ID",
        font=("Arial", 10, "bold"),
        bg="#FFFDF5"
    ).grid(
        row=1,
        column=0,
        padx=8,
        pady=7
    )

    cultivation_id_entry = tk.Entry(
        form_card,
        width=12,
        font=("Arial", 10)
    )
    cultivation_id_entry.grid(
        row=1,
        column=1,
        padx=8,
        pady=7
    )

    # Farm

    tk.Label(
        form_card,
        text="Farm",
        font=("Arial", 10, "bold"),
        bg="#FFFDF5"
    ).grid(
        row=1,
        column=2,
        padx=8,
        pady=7
    )

    farm_combo = ttk.Combobox(form_card,width=18, state="normal")
    farm_combo.grid(
        row=1,
        column=3,
        padx=8,
        pady=7
    )

    # Crop

    tk.Label(
        form_card,
        text="Crop",
        font=("Arial", 10, "bold"),
        bg="#FFFDF5"
    ).grid(
        row=1,
        column=4,
        padx=8,
        pady=7
    )

    crop_combo = ttk.Combobox(
        form_card,
        width=18,
        state="normal"
    )
    crop_combo.grid(
        row=1,
        column=5,
        padx=8,
        pady=7
    )

    # Sowing Date

    tk.Label(
        form_card,
        text="Sowing Date",
        font=("Arial", 10, "bold"),
        bg="#FFFDF5"
    ).grid(
        row=2,
        column=0,
        padx=8,
        pady=7
    )

    sowing_entry = tk.Entry(
        form_card,
        width=15,
        font=("Arial", 10)
    )
    sowing_entry.grid(
        row=2,
        column=1,
        padx=8,
        pady=7
    )

    # Harvest Date

    tk.Label(
        form_card,
        text="Harvest Date",
        font=("Arial", 10, "bold"),
        bg="#FFFDF5"
    ).grid(
        row=2,
        column=2,
        padx=8,
        pady=7
    )

    harvest_entry = tk.Entry(
        form_card,
        width=15,
        font=("Arial", 10)
    )
    harvest_entry.grid(
        row=2,
        column=3,
        padx=8,
        pady=7
    )

    # Expected Yield

    tk.Label(
        form_card,
        text="Expected Yield (kg)",
        font=("Arial", 10, "bold"),
        bg="#FFFDF5"
    ).grid(
        row=2,
        column=4,
        padx=8,
        pady=7
    )

    expected_entry = tk.Entry(
        form_card,
        width=15,
        font=("Arial", 10)
    )
    expected_entry.grid(
        row=2,
        column=5,
        padx=8,
        pady=7
    )

    # Actual Yield

    tk.Label(
        form_card,
        text="Actual Yield (kg)",
        font=("Arial", 10, "bold"),
        bg="#FFFDF5"
    ).grid(
        row=3,
        column=0,
        padx=8,
        pady=7
    )

    actual_entry = tk.Entry(
        form_card,
        width=15,
        font=("Arial", 10)
    )
    actual_entry.grid(
        row=3,
        column=1,
        padx=8,
        pady=7
    )

    tk.Label(
        form_card,
        text="Date format: YYYY-MM-DD",
        font=("Arial", 9),
        bg="#FFFDF5",
        fg="#777777"
    ).grid(
        row=3,
        column=2,
        columnspan=2,
        padx=5,
        pady=7
    )

    def clear_fields():

        cultivation_id_entry.delete(0, tk.END)
        farm_combo.set("")
        crop_combo.set("")
        sowing_entry.delete(0, tk.END)
        harvest_entry.delete(0, tk.END)
        expected_entry.delete(0, tk.END)
        actual_entry.delete(0, tk.END)

    def load_dropdowns():

        farms = view_farms()
        crops = view_crops()

        farm_values = []

        for farm in farms:
            farm_values.append(
                str(farm[0]) + " - " + str(farm[2])
            )

        crop_values = []

        for crop in crops:
            crop_values.append(
                str(crop[0]) + " - " + str(crop[1])
            )

        farm_combo["values"] = farm_values
        crop_combo["values"] = crop_values

        farm_filter["values"] = ["All"] + farm_values
        crop_filter["values"] = ["All"] + crop_values

        farm_filter.set("All")
        crop_filter.set("All")

    def load_cultivations():

        for item in cultivation_table.get_children():
            cultivation_table.delete(item)

        cultivations = view_cultivations()

        search_text = search_entry.get().lower()
        selected_farm = farm_filter.get()
        selected_crop = crop_filter.get()

        filtered = []

        for row in cultivations:

            cultivation_id = str(row[0])
            farm_id = str(row[1])
            crop_id = str(row[2])

            search_value = (
                    cultivation_id + " " +
                    farm_id + " " +
                    crop_id
            ).lower()

            if search_text not in search_value:
                continue

            if selected_farm != "All":

                selected_farm_id = selected_farm.split(" - ")[0]

                if farm_id != selected_farm_id:
                    continue

            if selected_crop != "All":

                selected_crop_id = selected_crop.split(" - ")[0]

                if crop_id != selected_crop_id:
                    continue

            filtered.append(row)

            display_row = (
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6]
            )

            cultivation_table.insert(
                "",
                tk.END,
                values=display_row
            )

        # Summary

        total_label.config(
            text=str(len(filtered))
        )

        completed = 0
        total_expected = 0
        total_actual = 0

        for row in filtered:

            if row[4] is not None:
                completed += 1

            if row[5] is not None:
                total_expected += float(row[5])

            if row[6] is not None:
                total_actual += float(row[6])

        harvest_label.config(
            text=str(completed)
        )

        expected_label.config(
            text=f"{total_expected:.2f} kg"
        )

        actual_label.config(
            text=f"{total_actual:.2f} kg"
        )

    def add_cultivation_data():
        farm_value = farm_combo.get().strip()
        crop_value = crop_combo.get().strip()
        sowing_date = sowing_entry.get().strip()
        harvest_date = harvest_entry.get().strip()
        expected_yield = expected_entry.get().strip()
        actual_yield = actual_entry.get().strip()

        if not farm_value or not crop_value:
            messagebox.showwarning(
                "Missing Information", "Please select or enter Farm and Crop IDs."
            )
            return

        farm_id = farm_value.split(" - ", 1)[0].strip()
        crop_id = crop_value.split(" - ", 1)[0].strip()
        if not farm_id.isdigit() or not crop_id.isdigit():
            messagebox.showwarning(
                "Invalid ID", "Farm ID and Crop ID must contain digits only."
            )
            return

        if not sowing_date or not expected_yield:
            messagebox.showwarning(
                "Missing Information", "Enter Sowing Date and Expected Yield."
            )
            return

        harvest_date = harvest_date or None
        actual_yield = actual_yield or None

        try:
            date.fromisoformat(sowing_date)
            if harvest_date is not None:
                date.fromisoformat(harvest_date)
            expected_number = float(expected_yield)
            actual_number = float(actual_yield) if actual_yield is not None else None
            if expected_number < 0 or (actual_number is not None and actual_number < 0):
                raise ValueError("Yield cannot be negative.")

            add_cultivation(
                farm_id, crop_id, sowing_date, harvest_date,
                expected_number, actual_number
            )
            messagebox.showinfo("Success", "Cultivation added successfully!")
            clear_fields()
            load_cultivations()
        except ValueError:
            messagebox.showerror(
                "Invalid Value",
                "Dates must use YYYY-MM-DD. Yield values must be non-negative numbers (kg)."
            )
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def update_cultivation_data():

        cultivation_id = cultivation_id_entry.get().strip()

        if cultivation_id == "":
            messagebox.showwarning(
                "Select Record",
                "Please select a cultivation record."
            )
            return

        farm_value = farm_combo.get()
        crop_value = crop_combo.get()
        sowing_date = sowing_entry.get().strip()
        harvest_date = harvest_entry.get().strip()
        expected_yield = expected_entry.get().strip()
        actual_yield = actual_entry.get().strip()

        if farm_value == "" or crop_value == "":
            messagebox.showwarning(
                "Missing Information",
                "Please select Farm and Crop."
            )
            return

        if sowing_date == "" or expected_yield == "":
            messagebox.showwarning(
                "Missing Information",
                "Please enter required details."
            )
            return

        farm_id = farm_value.split(" - ", 1)[0].strip()
        crop_id = crop_value.split(" - ", 1)[0].strip()
        if not farm_id.isdigit() or not crop_id.isdigit():
            messagebox.showwarning(
                "Invalid ID", "Farm ID and Crop ID must contain digits only."
            )
            return

        harvest_date = harvest_date or None
        actual_yield = actual_yield or None

        try:
            date.fromisoformat(sowing_date)
            if harvest_date is not None:
                date.fromisoformat(harvest_date)
            expected_number = float(expected_yield)
            actual_number = float(actual_yield) if actual_yield is not None else None
            if expected_number < 0 or (actual_number is not None and actual_number < 0):
                raise ValueError("Yield cannot be negative.")

            update_cultivation(
                cultivation_id,
                farm_id,
                crop_id,
                sowing_date,
                harvest_date,
                expected_number,
                actual_number
            )

            messagebox.showinfo(
                "Success",
                "Cultivation updated successfully!"
            )

            clear_fields()
            load_cultivations()

        except ValueError:

            messagebox.showerror(
                "Invalid Value",
                "Dates must use YYYY-MM-DD. Yield values must be non-negative numbers (kg)."
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def delete_cultivation_data():

        cultivation_id = cultivation_id_entry.get().strip()

        if cultivation_id == "":
            messagebox.showwarning(
                "Select Record",
                "Please select a cultivation record."
            )
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this cultivation record?"
        )

        if confirm:

            try:

                delete_cultivation(cultivation_id)

                messagebox.showinfo(
                    "Deleted",
                    "Cultivation record deleted successfully!"
                )

                clear_fields()
                load_cultivations()

            except Exception as e:

                messagebox.showerror(
                    "Error",
                    str(e)
                )

    def select_cultivation(event):

        selected = cultivation_table.selection()

        if not selected:
            return

        values = cultivation_table.item(
            selected[0],
            "values"
        )

        clear_fields()

        cultivation_id_entry.insert(
            0,
            values[0]
        )

        # Find farm
        farm_id = str(values[1])

        for value in farm_combo["values"]:

            if value.split(" - ")[0] == farm_id:
                farm_combo.set(value)
                break

        # Find crop
        crop_id = str(values[2])

        for value in crop_combo["values"]:

            if value.split(" - ")[0] == crop_id:
                crop_combo.set(value)
                break

        if values[3] != "None":
            sowing_entry.insert(
                0,
                values[3]
            )

        if values[4] != "None":
            harvest_entry.insert(
                0,
                values[4]
            )

        if values[5] != "None":
            expected_entry.insert(
                0,
                values[5]
            )

        if values[6] != "None":
            actual_entry.insert(
                0,
                values[6]
            )
    button_frame = tk.Frame(
        form_card,
        bg="#FFFDF5"
)
    button_frame.grid(
        row=3,
        column=2,
        columnspan=6,
        padx=10,
        pady=10
    )

    tk.Button(
        button_frame,
        text="➕ ADD",
        font=("Arial", 9, "bold"),
        bg="#2E7D32",
        fg="white",
        width=13,
        relief="flat",
        cursor="hand2",
        command=add_cultivation_data
    ).pack(side="left", padx=5)

    tk.Button(
        button_frame,
        text="✏ UPDATE",
        font=("Arial", 9, "bold"),
        bg="#558B2F",
        fg="white",
        width=13,
        relief="flat",
        cursor="hand2",
        command=update_cultivation_data
    ).pack(side="left", padx=5)

    tk.Button(
        button_frame,
        text="🗑 DELETE",
        font=("Arial", 9, "bold"),
        bg="#C62828",
        fg="white",
        width=13,
        relief="flat",
        cursor="hand2",
        command=delete_cultivation_data
    ).pack(side="left", padx=5)

    tk.Button(
        button_frame,
        text="CLEAR",
        font=("Arial", 9, "bold"),
        bg="#757575",
        fg="white",
        width=13,
        relief="flat",
        cursor="hand2",
        command=clear_fields
    ).pack(side="left", padx=5)

    #-----------------------------------------
    # TABLE
    #-----------------------------------------

    table_frame = tk.Frame(
        cultivation_window,
        bg="white",
        bd=1,
        relief="solid"
    )
    table_frame.pack(
        fill="both",
        expand=True,
        padx=32,
        pady=(0, 25)
    )

    tk.Label(
        table_frame,
        text="Cultivation Records",
        font=("Arial", 12, "bold"),
        bg="white",
        fg="#1B5E20"
    ).pack(
        anchor="w",
        padx=15,
        pady=10
    )

    tree_container = tk.Frame(
        table_frame,
        bg="white"
    )
    tree_container.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=(0, 15)
    )

    columns = (
        "ID",
        "Farm ID",
        "Crop ID",
        "Sowing Date",
        "Harvest Date",
        "Expected Yield (kg)",
        "Actual Yield (kg)"
    )

    cultivation_table = ttk.Treeview(
        tree_container,
        columns=columns,
        show="headings",
        height=7
    )

    for column in columns:

        cultivation_table.heading(
            column,
            text=column
        )

        cultivation_table.column(
            column,
            width=120,
            anchor="center"
        )

    scrollbar = ttk.Scrollbar(
        tree_container,
        orient="vertical",
        command=cultivation_table.yview
    )

    cultivation_table.configure(
        yscrollcommand=scrollbar.set
    )

    cultivation_table.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )

    cultivation_table.bind(
        "<ButtonRelease-1>",
        select_cultivation
    )

    search_entry.bind(
        "<KeyRelease>",
        lambda event: load_cultivations()
    )

    farm_filter.bind(
        "<<ComboboxSelected>>",
        lambda event: load_cultivations()
    )

    crop_filter.bind(
        "<<ComboboxSelected>>",
        lambda event: load_cultivations()
    )

    #-----------------------------------------
    # INITIAL LOAD
    #-----------------------------------------

    load_dropdowns()
    load_cultivations()
#=========================================
# CROP LOSS MANAGEMENT
#=========================================

def open_crop_loss_window(parent):
    win = tk.Frame(parent)
    win.pack(fill="both", expand=True)
    win.configure(bg="#F4F7F2")
    tk.Label(win,text="🌾 CROP LOSS MANAGEMENT",font=("Arial", 18, "bold"),bg="#1B5E20",fg="white",pady=15).pack(fill="x")
    form = tk.Frame(win,bg="#FFFDF5",bd=1,relief="solid")
    form.pack(fill="x", padx=25, pady=20)
    tk.Label(form,text="Cultivation ID",bg="#FFFDF5",font=("Arial", 10, "bold")).grid(row=0, column=0, padx=10, pady=10)
    cultivation_entry = tk.Entry(form, width=15)
    cultivation_entry.grid(row=0, column=1, padx=10)
    tk.Label(
        form,
        text="Loss Date",
        bg="#FFFDF5",
        font=("Arial", 10, "bold")
    ).grid(row=0, column=2, padx=10)

    date_entry = tk.Entry(form, width=15)
    date_entry.grid(row=0, column=3, padx=10)
    tk.Label(
        form,
        text="Loss Quantity",
        bg="#FFFDF5",
        font=("Arial", 10, "bold")
    ).grid(row=1, column=0, padx=10, pady=10)

    quantity_entry = tk.Entry(form, width=15)
    quantity_entry.grid(row=1, column=1, padx=10)

    tk.Label(
        form,
        text="Loss %",
        bg="#FFFDF5",
        font=("Arial", 10, "bold")
    ).grid(row=1, column=2, padx=10)

    percentage_entry = tk.Entry(form, width=15)
    percentage_entry.grid(row=1, column=3, padx=10)

    tk.Label(
        form,
        text="Reason ID",
        bg="#FFFDF5",
        font=("Arial", 10, "bold")
    ).grid(row=2, column=0, padx=10, pady=10)

    reason_entry = tk.Entry(form, width=15)
    reason_entry.grid(row=2, column=1, padx=10)

    # Buttons
    def clear_fields():
        for entry in (
            cultivation_entry,
            date_entry,
            quantity_entry,
            percentage_entry,
            reason_entry
        ):
            entry.delete(0, tk.END)

    def add_loss():

        if cultivation_entry.get() == "" or percentage_entry.get() == "":
            messagebox.showwarning(
                "Missing",
                "Enter Cultivation ID and Loss %"
            )
            return

        try:
            add_crop_loss(
                cultivation_entry.get(),
                date_entry.get(),
                quantity_entry.get(),
                percentage_entry.get(),
                reason_entry.get()
            )

            messagebox.showinfo(
                "Success",
                "Crop loss recorded successfully!"
            )

            clear_fields()
            load_data()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_loss():

        selected = table.selection()

        if not selected:
            messagebox.showwarning(
                "Select",
                "Select a loss record first."
            )
            return

        values = table.item(
            selected[0],
            "values"
        )

        try:
            delete_crop_loss(values[0])

            messagebox.showinfo(
                "Deleted",
                "Loss record deleted."
            )

            load_data()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(
        form,
        text="ADD LOSS",
        bg="#2E7D32",
        fg="white",
        width=15,
        relief="flat",
        command=add_loss
    ).grid(row=2, column=2, padx=10, pady=10)

    tk.Button(
        form,
        text="CLEAR",
        bg="#757575",
        fg="white",
        width=15,
        relief="flat",
        command=clear_fields
    ).grid(row=2, column=3, padx=10)

    # Table
    table_frame = tk.Frame(win, bg="white")
    table_frame.pack(
        fill="both",
        expand=True,
        padx=25,
        pady=(0, 20)
    )

    columns = (
        "ID",
        "Cultivation ID",
        "Date",
        "Quantity (kg)",
        "Loss (%)",
        "Reason ID"
    )

    table = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings"
    )

    for column in columns:
        table.heading(column, text=column)
        table.column(
            column,
            width=130,
            anchor="center"
        )

    table.pack(
        fill="both",
        expand=True
    )

    def load_data():

        for item in table.get_children():
            table.delete(item)

        losses = view_crop_losses()

        for loss in losses:
            display_loss = (
                loss[0],
                loss[1],
                loss[2],
                loss[3],
                loss[4],
                loss[5]
            )
            table.insert(
                "",
                tk.END,
                values=display_loss
            )

    load_data()
#=========================================
# LOSS REASON MANAGEMENT
#=========================================

def open_loss_reason_window(parent):

    win = tk.Frame(parent)
    win.pack(fill="both", expand=True)
    win.configure(bg="#F4F7F2")

    # Header
    tk.Label(
        win,
        text="⚠ LOSS REASON MANAGEMENT",
        font=("Arial", 18, "bold"),
        bg="#1B5E20",
        fg="white",
        pady=15
    ).pack(fill="x")

    # Form
    form = tk.Frame(
        win,
        bg="#FFFDF5",
        bd=1,
        relief="solid"
    )
    form.pack(
        fill="x",
        padx=25,
        pady=20
    )

    tk.Label(
        form,
        text="Reason ID",
        bg="#FFFDF5",
        font=("Arial", 10, "bold")
    ).grid(row=0, column=0, padx=10, pady=10)

    id_entry = tk.Entry(form, width=15)
    id_entry.grid(row=0, column=1, padx=10)

    tk.Label(
        form,
        text="Reason Name",
        bg="#FFFDF5",
        font=("Arial", 10, "bold")
    ).grid(row=0, column=2, padx=10)

    name_entry = tk.Entry(form, width=20)
    name_entry.grid(row=0, column=3, padx=10)

    tk.Label(
        form,
        text="Description",
        bg="#FFFDF5",
        font=("Arial", 10, "bold")
    ).grid(row=1, column=0, padx=10, pady=10)

    description_entry = tk.Entry(form, width=50)
    description_entry.grid(
        row=1,
        column=1,
        columnspan=3,
        padx=10
    )

    def clear_fields():

        id_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        description_entry.delete(0, tk.END)

    def load_data():

        for item in table.get_children():
            table.delete(item)

        reasons = view_loss_reasons()

        for reason in reasons:
            table.insert(
                "",
                tk.END,
                values=reason
            )

    def add_reason():

        name = name_entry.get().strip()
        description = description_entry.get().strip()

        if name == "":
            messagebox.showwarning(
                "Missing",
                "Enter loss reason."
            )
            return
        if len(name) < 3:
            messagebox.showwarning(
                "Invalid",
                "Loss reason must contain at least 3 characters."
            )
            return
        try:

            add_loss_reason(
                name,
                description
            )

            messagebox.showinfo(
                "Success",
                "Loss reason added successfully!"
            )

            clear_fields()
            load_data()

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e)
            )

    def update_reason():

        reason_id = id_entry.get().strip()

        if reason_id == "":
            messagebox.showwarning(
                "Select",
                "Select a reason first."
            )
            return

        try:

            update_loss_reason(
                reason_id,
                name_entry.get(),
                description_entry.get()
            )

            messagebox.showinfo(
                "Success",
                "Loss reason updated!"
            )

            clear_fields()
            load_data()

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e)
            )

    def delete_reason():

        reason_id = id_entry.get().strip()

        if reason_id == "":
            messagebox.showwarning(
                "Select",
                "Select a reason first."
            )
            return

        confirm = messagebox.askyesno(
            "Confirm",
            "Delete this loss reason?"
        )

        if confirm:

            try:

                delete_loss_reason(reason_id)

                messagebox.showinfo(
                    "Deleted",
                    "Loss reason deleted!"
                )

                clear_fields()
                load_data()

            except Exception as e:
                messagebox.showerror(
                    "Error",
                    "This reason may be used in crop loss records.\n\n"
                    + str(e)
                )

    # Buttons
    tk.Button(
        form,
        text="ADD",
        bg="#2E7D32",
        fg="white",
        width=12,
        relief="flat",
        command=add_reason
    ).grid(row=2, column=0, padx=10, pady=12)

    tk.Button(
        form,
        text="UPDATE",
        bg="#558B2F",
        fg="white",
        width=12,
        relief="flat",
        command=update_reason
    ).grid(row=2, column=1, padx=10)

    tk.Button(
        form,
        text="DELETE",
        bg="#C62828",
        fg="white",
        width=12,
        relief="flat",
        command=delete_reason
    ).grid(row=2, column=2, padx=10)

    tk.Button(
        form,
        text="CLEAR",
        bg="#757575",
        fg="white",
        width=12,
        relief="flat",
        command=clear_fields
    ).grid(row=2, column=3, padx=10)

    # Table
    table_frame = tk.Frame(win, bg="white")
    table_frame.pack(
        fill="both",
        expand=True,
        padx=25,
        pady=(0, 20)
    )

    columns = (
        "Reason ID",
        "Reason Name",
        "Description"
    )

    table = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings"
    )

    table.heading("Reason ID", text="Reason ID")
    table.heading("Reason Name", text="Reason Name")
    table.heading("Description", text="Description")

    table.column(
        "Reason ID",
        width=100,
        anchor="center"
    )

    table.column(
        "Reason Name",
        width=200,
        anchor="center"
    )

    table.column(
        "Description",
        width=450,
        anchor="w"
    )

    table.pack(
        fill="both",
        expand=True
    )

    def select_reason(event):

        selected = table.selection()

        if not selected:
            return

        values = table.item(
            selected[0],
            "values"
        )

        clear_fields()

        id_entry.insert(0, values[0])
        name_entry.insert(0, values[1])
        description_entry.insert(0, values[2])

    table.bind(
        "<ButtonRelease-1>",
        select_reason
    )

    load_data()
#=========================================
# PREVENTION MEASURE MANAGEMENT
#=========================================

def open_prevention_window(parent):
    for child in parent.winfo_children():
        child.destroy()
    win = tk.Frame(parent, bg="#F4F7F2")
    win.pack(fill="both", expand=True)
    tk.Label(win, text="🛡 PREVENTION MEASURE MANAGEMENT", font=("Arial", 18, "bold"),
             bg="#1B5E20", fg="white", pady=15).pack(fill="x")

    form = tk.Frame(win, bg="#FFFDF5", bd=1, relief="solid")
    form.pack(fill="x", padx=25, pady=20)
    tk.Label(form, text="Prevention ID", bg="#FFFDF5", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=10, pady=10)
    id_entry = tk.Entry(form, width=15)
    id_entry.grid(row=0, column=1, padx=10)
    tk.Label(form, text="Reason ID", bg="#FFFDF5", font=("Arial", 10, "bold")).grid(row=0, column=2, padx=10)
    reason_entry = tk.Entry(form, width=15)
    reason_entry.grid(row=0, column=3, padx=10)
    tk.Label(form, text="Prevention Action", bg="#FFFDF5", font=("Arial", 10, "bold")).grid(row=1, column=0, padx=10, pady=10)
    action_entry = tk.Entry(form, width=70)
    action_entry.grid(row=1, column=1, columnspan=3, padx=10, sticky="ew")
    form.grid_columnconfigure(3, weight=1)

    def clear_fields():
        id_entry.delete(0, tk.END)
        reason_entry.delete(0, tk.END)
        action_entry.delete(0, tk.END)

    def select_measure(measure):
        clear_fields()
        id_entry.insert(0, str(measure[0]))
        reason_entry.insert(0, str(measure[1]))
        action_entry.insert(0, str(measure[2]))

    def load_data():
        for child in rows_frame.winfo_children():
            child.destroy()
        reasons = view_loss_reasons()
        measures = view_prevention_measures()
        reason_names = {int(row[0]): str(row[1]) for row in reasons}
        grouped = {}
        for measure in measures:
            grouped.setdefault(int(measure[1]), []).append(measure)

        if not reasons:
            tk.Label(rows_frame, text="Add Loss Reasons first; prevention actions are grouped under each reason.",
                     bg="white", fg="#666666", font=("Arial", 11), pady=18).pack(fill="x")
            return

        for reason_id, reason_name in sorted(reason_names.items()):
            group = grouped.get(reason_id, [])
            row_frame = tk.Frame(rows_frame, bg="#E8F5E9", bd=1, relief="solid")
            row_frame.pack(fill="x", padx=5, pady=4)
            row_frame.grid_columnconfigure(3, weight=1)
            ids_text = ", ".join(str(item[0]) for item in group) if group else "—"
            tk.Label(row_frame, text=ids_text, bg="#E8F5E9", fg="#333333", width=16,
                     anchor="center", justify="center").grid(row=0, column=0, padx=5, pady=7, sticky="nsew")
            tk.Label(row_frame, text=str(reason_id), bg="#E8F5E9", fg="#333333", width=9,
                     anchor="center").grid(row=0, column=1, padx=5, pady=7, sticky="nsew")
            tk.Label(row_frame, text=reason_name, bg="#E8F5E9", fg="#1B5E20", width=23,
                     font=("Arial", 10, "bold"), anchor="w", justify="left", wraplength=190
                     ).grid(row=0, column=2, padx=6, pady=7, sticky="nsew")
            actions_frame = tk.Frame(row_frame, bg="#E8F5E9")
            actions_frame.grid(row=0, column=3, padx=5, pady=5, sticky="nsew")
            for action_column in range(max(1, len(group))):
                actions_frame.grid_columnconfigure(action_column, weight=1, uniform=f"reason_{reason_id}")
            if group:
                action_labels = []
                for index, measure in enumerate(group):
                    label = tk.Label(actions_frame, text=f"{index + 1}. {measure[2]}",
                                     bg="white", fg="#333333", anchor="w", justify="left",
                                     wraplength=390, padx=9, pady=8, bd=1, relief="solid", cursor="hand2")
                    label.grid(row=0, column=index, padx=4, pady=2, sticky="nsew")
                    label.bind("<Button-1>", lambda _event, item=measure: select_measure(item))
                    action_labels.append(label)
                def resize_actions(event, labels=action_labels):
                    width = max(220, (event.width // max(1, len(labels))) - 18)
                    for action_label in labels:
                        action_label.configure(wraplength=width)
                actions_frame.bind("<Configure>", resize_actions)
            else:
                tk.Label(actions_frame, text="No prevention measures added for this reason yet.",
                         bg="#E8F5E9", fg="#777777", anchor="w", padx=8, pady=10
                         ).grid(row=0, column=0, sticky="ew")

    def add_measure():
        reason_id = reason_entry.get().strip()
        action = action_entry.get().strip()
        if not reason_id.isdigit() or not action:
            messagebox.showwarning("Missing or invalid data", "Enter a numeric Reason ID and a Prevention Action.", parent=win)
            return
        if int(reason_id) not in {int(row[0]) for row in view_loss_reasons()}:
            messagebox.showwarning("Invalid Reason ID", "That Reason ID does not exist in Loss_Reason.", parent=win)
            return
        try:
            add_prevention_measure(int(reason_id), action)
            clear_fields()
            load_data()
            messagebox.showinfo("Success", "Prevention measure added.", parent=win)
        except Exception as error:
            messagebox.showerror("Error", str(error), parent=win)

    def update_measure():
        prevention_id = id_entry.get().strip()
        reason_id = reason_entry.get().strip()
        action = action_entry.get().strip()
        if not prevention_id.isdigit() or not reason_id.isdigit() or not action:
            messagebox.showwarning("Select a measure", "Click a prevention action first, then edit its fields.", parent=win)
            return
        try:
            update_prevention_measure(int(prevention_id), int(reason_id), action)
            clear_fields()
            load_data()
            messagebox.showinfo("Success", "Prevention measure updated.", parent=win)
        except Exception as error:
            messagebox.showerror("Error", str(error), parent=win)

    def delete_measure():
        prevention_id = id_entry.get().strip()
        if not prevention_id.isdigit():
            messagebox.showwarning("Select a measure", "Click the prevention action you want to delete.", parent=win)
            return
        if messagebox.askyesno("Confirm", "Delete this prevention measure?", parent=win):
            try:
                delete_prevention_measure(int(prevention_id))
                clear_fields()
                load_data()
            except Exception as error:
                messagebox.showerror("Error", str(error), parent=win)

    buttons = (("ADD", "#2E7D32", add_measure), ("UPDATE", "#558B2F", update_measure),
               ("DELETE", "#C62828", delete_measure), ("CLEAR", "#757575", clear_fields))
    for column, (title, color, command) in enumerate(buttons):
        tk.Button(form, text=title, bg=color, fg="white", width=12, relief="flat",
                  cursor="hand2", command=command).grid(row=2, column=column, padx=10, pady=12)

    table_frame = tk.Frame(win, bg="white", bd=1, relief="solid")
    table_frame.pack(fill="both", expand=True, padx=25, pady=(0, 20))
    header = tk.Frame(table_frame, bg="#DDEBDD")
    header.pack(fill="x")
    header.grid_columnconfigure(3, weight=1)
    header_columns = (("Prevention IDs", 16), ("Reason ID", 9), ("Loss Reason", 23),
                      ("Prevention Measures — click an action to edit", None))
    for column, (title, width) in enumerate(header_columns):
        options = {"text": title, "bg": "#DDEBDD", "fg": "#1B5E20",
                   "font": ("Arial", 10, "bold"), "anchor": "w" if column >= 2 else "center",
                   "padx": 8, "pady": 8}
        if width is not None:
            options["width"] = width
        tk.Label(header, **options).grid(row=0, column=column, sticky="ew")
    body = tk.Frame(table_frame, bg="white")
    body.pack(fill="both", expand=True)
    table_canvas = tk.Canvas(body, bg="white", highlightthickness=0)
    vertical_scrollbar = ttk.Scrollbar(body, orient="vertical", command=table_canvas.yview)
    table_canvas.configure(yscrollcommand=vertical_scrollbar.set)
    vertical_scrollbar.pack(side="right", fill="y")
    table_canvas.pack(side="left", fill="both", expand=True)
    rows_frame = tk.Frame(table_canvas, bg="white")
    rows_window = table_canvas.create_window((0, 0), window=rows_frame, anchor="nw")
    rows_frame.bind("<Configure>", lambda _event: table_canvas.configure(scrollregion=table_canvas.bbox("all")))
    table_canvas.bind("<Configure>", lambda event: table_canvas.itemconfigure(rows_window, width=event.width))
    load_data()
#=========================================
# ANALYTICS DASHBOARD
#=========================================
def open_analytics_window(parent, selected_farmer_ids=None, on_filter=None):
    # Keep one report page in the container even if this function is called twice.
    for child in parent.winfo_children():
        child.destroy()
    page = tk.Frame(parent, bg="#F4F7F2")
    page.pack(fill="both", expand=True)
    tk.Label(page, text="📊 CROP LOSS ANALYTICS", font=("Arial", 20, "bold"),
             bg="#1B5E20", fg="white", pady=16).pack(fill="x")

    body = tk.Frame(page, bg="#F4F7F2")
    body.pack(fill="both", expand=True)
    canvas = tk.Canvas(body, bg="#F4F7F2", highlightthickness=0)
    scrollbar = ttk.Scrollbar(body, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    content = tk.Frame(canvas, bg="#F4F7F2")
    content_window = canvas.create_window((0, 0), window=content, anchor="nw")
    content.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.bind("<Configure>", lambda event: canvas.itemconfigure(content_window, width=event.width))

    farmers = view_farmers()
    farmer_names = {int(row[0]): str(row[1]) for row in farmers}
    if selected_farmer_ids is None:
        selected_ids = set()
    elif isinstance(selected_farmer_ids, (int, str)):
        selected_ids = {int(selected_farmer_ids)}
    else:
        selected_ids = {int(value) for value in selected_farmer_ids}

    filter_bar = tk.Frame(content, bg="#E8F5E9", bd=1, relief="solid")
    filter_bar.pack(fill="x", padx=22, pady=(14, 2))
    tk.Label(filter_bar, text="Filter by farmer (select multiple):", bg="#E8F5E9", fg="#1B5E20",
             font=("Arial", 11, "bold")).pack(anchor="w", padx=14, pady=(9, 3))
    selection_row = tk.Frame(filter_bar, bg="#E8F5E9")
    selection_row.pack(fill="x", padx=12, pady=(0, 8))
    list_frame = tk.Frame(selection_row, bg="#E8F5E9")
    list_frame.pack(side="left")
    farmer_listbox = tk.Listbox(list_frame, selectmode=tk.MULTIPLE, exportselection=False,
                                height=min(4, max(2, len(farmers))), width=38,
                                font=("Arial", 10), activestyle="dotbox")
    list_scroll = ttk.Scrollbar(list_frame, orient="vertical", command=farmer_listbox.yview)
    farmer_listbox.configure(yscrollcommand=list_scroll.set)
    farmer_listbox.pack(side="left")
    list_scroll.pack(side="right", fill="y")
    for index, farmer in enumerate(farmers):
        farmer_listbox.insert(tk.END, f"{farmer[1]} (ID {farmer[0]})")
        if int(farmer[0]) in selected_ids:
            farmer_listbox.selection_set(index)

    filter_actions = tk.Frame(selection_row, bg="#E8F5E9")
    filter_actions.pack(side="left", anchor="n", padx=12)
    filter_status = tk.Label(filter_actions, text="No filter applied — showing all farmers.",
                             bg="#E8F5E9", fg="#555555", font=("Arial", 9, "italic"), wraplength=380)
    filter_status.pack(anchor="w", pady=(2, 8))

    def apply_filter(clear=False):
        chosen_ids = ([] if clear else
                      [int(farmers[index][0]) for index in farmer_listbox.curselection()])
        if on_filter:
            on_filter(chosen_ids or None)
        else:
            open_analytics_window(parent, chosen_ids or None)

    tk.Button(filter_actions, text="Apply Selected Farmers", bg="#2E7D32", fg="white",
              relief="flat", cursor="hand2", command=lambda: apply_filter()).pack(side="left", padx=(0, 8))
    tk.Button(filter_actions, text="Show All", bg="#607D8B", fg="white",
              relief="flat", cursor="hand2", command=lambda: apply_filter(clear=True)).pack(side="left")
    tk.Button(filter_actions, text="Refresh", bg="#1976D2", fg="white",
              relief="flat", cursor="hand2", command=lambda: apply_filter()).pack(side="left", padx=(8, 0))
    if selected_ids:
        filter_status.configure(text=f"Showing {len(selected_ids)} selected farmer(s).")

    reasons = view_loss_reasons()
    reason_names = {int(row[0]): str(row[1]) for row in reasons}
    measures = view_prevention_measures()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            SELECT cl.loss_id, cl.loss_quantity, cl.loss_percentage,
                   cl.reason_id, lr.reason_name, c.season, fr.farmer_name,
                   fr.farmer_id, fm.farm_id, fm.farm_name
            FROM Crop_Loss AS cl
            LEFT JOIN Cultivation AS cu ON cu.cultivation_id = cl.cultivation_id
            LEFT JOIN Crop AS c ON c.crop_id = cu.crop_id
            LEFT JOIN Farm AS fm ON fm.farm_id = cu.farm_id
            LEFT JOIN Farmer AS fr ON fr.farmer_id = fm.farmer_id
            LEFT JOIN Loss_Reason AS lr ON lr.reason_id = cl.reason_id
            ORDER BY cl.loss_id
        """)
        all_loss_rows = cursor.fetchall()
        count_query = """
            SELECT COUNT(DISTINCT fm.farm_id), COUNT(DISTINCT cu.cultivation_id)
            FROM Farmer AS fr
            LEFT JOIN Farm AS fm ON fm.farmer_id = fr.farmer_id
            LEFT JOIN Cultivation AS cu ON cu.farm_id = fm.farm_id
        """
        if selected_ids:
            placeholders = ",".join(["%s"] * len(selected_ids))
            count_query += f" WHERE fr.farmer_id IN ({placeholders})"
            cursor.execute(count_query, tuple(sorted(selected_ids)))
        else:
            cursor.execute(count_query)
        farm_cultivation_counts = cursor.fetchone() or (0, 0)

        farm_query = """
            SELECT fr.farmer_id, fr.farmer_name, fm.farm_id, fm.farm_name,
                   COALESCE(SUM(cl.loss_quantity), 0)
            FROM Farmer AS fr
            LEFT JOIN Farm AS fm ON fm.farmer_id = fr.farmer_id
            LEFT JOIN Cultivation AS cu ON cu.farm_id = fm.farm_id
            LEFT JOIN Crop_Loss AS cl ON cl.cultivation_id = cu.cultivation_id
        """
        if selected_ids:
            placeholders = ",".join(["%s"] * len(selected_ids))
            farm_query += f" WHERE fr.farmer_id IN ({placeholders})"
            farm_query += " GROUP BY fr.farmer_id, fr.farmer_name, fm.farm_id, fm.farm_name ORDER BY fr.farmer_id, fm.farm_id"
            cursor.execute(farm_query, tuple(sorted(selected_ids)))
        else:
            farm_query += " GROUP BY fr.farmer_id, fr.farmer_name, fm.farm_id, fm.farm_name ORDER BY fr.farmer_id, fm.farm_id"
            cursor.execute(farm_query)
        farm_comparison_rows = cursor.fetchall()
    finally:
        cursor.close()

    analytics_rows = [
        row for row in all_loss_rows
        if not selected_ids or row[7] in selected_ids
    ]
    loss_counts = {}
    loss_quantities = {}
    season_reason_counts = {}
    total_quantity = 0.0
    percentage_sum = 0.0
    percentage_count = 0
    for row in analytics_rows:
        quantity = float(row[1] or 0)
        reason_name = row[4] or reason_names.get(row[3], f"Reason {row[3]}")
        total_quantity += quantity
        loss_counts[reason_name] = loss_counts.get(reason_name, 0) + 1
        loss_quantities[reason_name] = loss_quantities.get(reason_name, 0.0) + quantity
        if row[2] is not None:
            percentage_sum += float(row[2])
            percentage_count += 1
        season = str(row[5]) if row[5] else "Unknown Season"
        season_reason_counts.setdefault(season, {})
        season_reason_counts[season][reason_name] = season_reason_counts[season].get(reason_name, 0) + 1

    average_percentage = percentage_sum / percentage_count if percentage_count else 0.0
    farms_count, cultivations_count = (int(value or 0) for value in farm_cultivation_counts)
    tk.Label(content, text="↓ Scroll down for four charts, insights, and prevention measures",
             font=("Arial", 10, "italic"), bg="#F4F7F2", fg="#555555").pack(
                 anchor="e", padx=24, pady=(8, 0))

    kpi_frame = tk.Frame(content, bg="#F4F7F2")
    kpi_frame.pack(fill="x", padx=22, pady=12)
    kpis = (("LOSS RECORDS", str(len(analytics_rows))),
            ("TOTAL LOSS", f"{total_quantity:,.2f} kg"),
            ("AVERAGE LOSS", f"{average_percentage:.2f}%"),
            ("FARMS", str(farms_count)))
    for title, value in kpis:
        card = tk.Frame(kpi_frame, bg="white", bd=1, relief="solid")
        card.pack(side="left", fill="both", expand=True, padx=5)
        tk.Label(card, text=title, font=("Arial", 10, "bold"), bg="white", fg="#666666").pack(pady=(11, 3))
        tk.Label(card, text=value, font=("Arial", 17, "bold"), bg="white", fg="#1B5E20").pack(pady=(0, 11))

    chart_card = tk.Frame(content, bg="white", bd=1, relief="solid")
    chart_card.pack(fill="x", padx=22, pady=(0, 16))

    def add_chart_heading(title):
        tk.Label(chart_card, text=title, font=("Arial", 14, "bold"),
                 bg="white", fg="#1B5E20").pack(anchor="w", padx=16, pady=(13, 4))

    add_chart_heading("Graph 1: Loss Records by Reason")
    record_names = list(loss_counts)
    if record_names:
        fig = Figure(figsize=(9.5, max(3.2, 2.5 + 0.18 * len(record_names))), dpi=80, facecolor="white")
        ax = fig.add_subplot(111)
        wedges, _ = ax.pie([loss_counts[name] for name in record_names], startangle=90,
                           wedgeprops={"width": 0.42})
        ax.legend(wedges, [f"{name}: {loss_counts[name]}" for name in record_names],
                  title="Reason (records)", loc="center left", bbox_to_anchor=(0.98, 0.5), fontsize=8)
        ax.set_aspect("equal")
        fig.tight_layout()
        chart = FigureCanvasTkAgg(fig, master=chart_card)
        chart.draw()
        chart.get_tk_widget().pack(fill="x", padx=12, pady=(0, 14))
    else:
        tk.Label(chart_card, text="No loss records for this selection.", bg="white").pack(anchor="w", padx=16, pady=8)

    add_chart_heading("Graph 2: Loss Quantity by Reason")
    quantity_items = sorted(loss_quantities.items(), key=lambda item: item[1], reverse=True)
    if quantity_items:
        fig = Figure(figsize=(9.5, max(2.8, 0.38 * len(quantity_items) + 1)), dpi=80, facecolor="white")
        ax = fig.add_subplot(111)
        ax.barh([item[0] for item in quantity_items], [item[1] for item in quantity_items], color="#8D6E63")
        ax.invert_yaxis()
        ax.set_xlabel("Loss quantity (kg)")
        ax.grid(axis="x", alpha=0.25)
        fig.tight_layout()
        chart = FigureCanvasTkAgg(fig, master=chart_card)
        chart.draw()
        chart.get_tk_widget().pack(fill="x", padx=12, pady=(0, 14))
    else:
        tk.Label(chart_card, text="No loss quantities for this selection.", bg="white").pack(anchor="w", padx=16, pady=8)

    add_chart_heading("Graph 3: Season-wise Loss Reason")
    season_names = sorted(season_reason_counts)
    reason_labels = sorted({reason for values in season_reason_counts.values() for reason in values})
    if season_names and reason_labels:
        matrix = [[season_reason_counts.get(season, {}).get(reason, 0) for season in season_names]
                  for reason in reason_labels]
        fig = Figure(figsize=(9.5, max(3.0, 0.38 * len(reason_labels) + 1.2)), dpi=80, facecolor="white")
        ax = fig.add_subplot(111)
        heat = ax.imshow(matrix, aspect="auto", cmap="YlGn")
        ax.set_xticks(range(len(season_names)))
        ax.set_xticklabels(season_names, rotation=20, ha="right")
        ax.set_yticks(range(len(reason_labels)))
        ax.set_yticklabels(reason_labels, fontsize=8)
        ax.set_xlabel("Crop season")
        ax.set_ylabel("Loss reason")
        for i, values in enumerate(matrix):
            for j, value in enumerate(values):
                ax.text(j, i, str(value), ha="center", va="center", fontsize=8)
        fig.colorbar(heat, ax=ax, label="Loss records")
        fig.tight_layout()
        chart = FigureCanvasTkAgg(fig, master=chart_card)
        chart.draw()
        chart.get_tk_widget().pack(fill="x", padx=12, pady=(0, 14))
    else:
        tk.Label(chart_card, text="No season data for this selection.", bg="white").pack(anchor="w", padx=16, pady=8)

    # Show all farmers when unfiltered, farms for one farmer, or each selected
    # farmer's total when several farmers have been selected.
    if not selected_ids:
        add_chart_heading("Graph 4: Farmer-wise Loss Quantity")
        totals = {}
        for row in all_loss_rows:
            if row[7] is not None:
                key = (int(row[7]), str(row[6] or f"Farmer {row[7]}"))
                totals[key] = totals.get(key, 0.0) + float(row[1] or 0)
        chart_labels = [f"{name} (ID {farmer_id})" for (farmer_id, name) in sorted(totals)]
        chart_values = [totals[key] for key in sorted(totals)]
    elif len(selected_ids) == 1:
        selected_id = next(iter(selected_ids))
        add_chart_heading(f"Graph 4: Farm-wise Loss Quantity — {farmer_names.get(selected_id, 'Selected Farmer')}")
        totals = {}
        for row in analytics_rows:
            if row[8] is not None:
                key = (int(row[8]), str(row[9] or f"Farm {row[8]}"))
                totals[key] = totals.get(key, 0.0) + float(row[1] or 0)
        chart_labels = [f"{name} (ID {farm_id})" for farm_id, name in sorted(totals)]
        chart_values = [totals[key] for key in sorted(totals)]
    else:
        add_chart_heading("Graph 4: Loss Quantity by Selected Farmer")
        totals = {}
        for row in analytics_rows:
            if row[7] is not None:
                key = (int(row[7]), str(row[6] or f"Farmer {row[7]}"))
                totals[key] = totals.get(key, 0.0) + float(row[1] or 0)
        chart_labels = [f"{name} (ID {farmer_id})" for farmer_id, name in sorted(totals)]
        chart_values = [totals[key] for key in sorted(totals)]
    if chart_labels:
        fig = Figure(figsize=(9.5, max(2.8, 0.38 * len(chart_labels) + 1)), dpi=80, facecolor="white")
        ax = fig.add_subplot(111)
        ax.barh(chart_labels, chart_values, color="#4F8A8B")
        ax.invert_yaxis()
        ax.set_xlabel("Loss quantity (kg)")
        ax.grid(axis="x", alpha=0.25)
        fig.tight_layout()
        chart = FigureCanvasTkAgg(fig, master=chart_card)
        chart.draw()
        chart.get_tk_widget().pack(fill="x", padx=12, pady=(0, 14))
    else:
        tk.Label(chart_card, text="No farm loss data for this selection.", bg="white").pack(anchor="w", padx=16, pady=8)

    insight = tk.Frame(content, bg="#F1F8E9", bd=1, relief="solid")
    insight.pack(fill="x", padx=22, pady=(0, 16))
    tk.Label(insight, text="Insights", font=("Arial", 14, "bold"), bg="#F1F8E9", fg="#1B5E20").pack(anchor="w", padx=16, pady=(12, 5))
    # Build ranked comparisons from the filtered loss rows, not one global reason.
    farmer_totals = {}
    farmer_reasons = {}
    farmer_seasons = {}
    for row in analytics_rows:
        if row[7] is None:
            continue
        farmer_id = int(row[7])
        quantity = float(row[1] or 0)
        reason_name = row[4] or reason_names.get(row[3], f"Reason {row[3]}")
        season_name = str(row[5]) if row[5] else "Unknown season"
        farmer_totals[farmer_id] = farmer_totals.get(farmer_id, 0.0) + quantity
        farmer_reasons.setdefault(farmer_id, {})
        farmer_reasons[farmer_id][reason_name] = farmer_reasons[farmer_id].get(reason_name, 0.0) + quantity
        farmer_seasons.setdefault(farmer_id, {})
        farmer_seasons[farmer_id][season_name] = farmer_seasons[farmer_id].get(season_name, 0.0) + quantity

    farmer_farms = {}
    for row in farm_comparison_rows:
        farmer_id = int(row[0])
        if row[2] is not None:
            farmer_farms.setdefault(farmer_id, []).append((str(row[3] or f"Farm {row[2]}"), float(row[4] or 0)))

    season_totals = {}
    for row in analytics_rows:
        season_name = str(row[5]) if row[5] else "Unknown season"
        season_totals[season_name] = season_totals.get(season_name, 0.0) + float(row[1] or 0)

    insight_lines = []
    if not analytics_rows:
        if selected_ids:
            names = ", ".join(f"{farmer_names.get(fid, f'Farmer {fid}')} (ID {fid})" for fid in sorted(selected_ids))
            insight_lines.append(f"No loss records found for {names}. Check the Crop_Loss → Cultivation → Farm → Farmer links.")
        else:
            insight_lines.append("No crop-loss records are available yet.")
    else:
        frequent_reason = max(loss_counts.items(), key=lambda item: item[1])
        highest_quantity_reason = max(loss_quantities.items(), key=lambda item: item[1])
        insight_lines.append(
            f"• Loss reasons: {frequent_reason[0]} is most frequent ({frequent_reason[1]} records); "
            f"{highest_quantity_reason[0]} has the highest total quantity ({highest_quantity_reason[1]:,.2f} kg)."
        )
        insight_lines.append(
            f"• Yield impact: {total_quantity:,.2f} kg total loss across {len(analytics_rows)} records; "
            f"average recorded loss is {average_percentage:.2f}%."
        )
        ordered_seasons = sorted(season_totals.items(), key=lambda item: (-item[1], item[0].casefold()))
        season_summary = "; ".join(f"{season}: {amount:,.2f} kg" for season, amount in ordered_seasons)
        insight_lines.append(
            f"• Season pattern: highest loss is in {ordered_seasons[0][0]} ({ordered_seasons[0][1]:,.2f} kg). "
            f"Season totals — {season_summary}."
        )

        if selected_ids:
            ranked_ids = sorted(selected_ids,
                                key=lambda fid: (-farmer_totals.get(fid, 0.0), farmer_names.get(fid, "").casefold(), fid))
            farmer_summaries = []
            for rank, farmer_id in enumerate(ranked_ids, start=1):
                name = farmer_names.get(farmer_id, f"Farmer {farmer_id}")
                total = farmer_totals.get(farmer_id, 0.0)
                reasons_for_farmer = farmer_reasons.get(farmer_id, {})
                main_reason = max(reasons_for_farmer.items(), key=lambda item: item[1])[0] if reasons_for_farmer else "no linked loss reason"
                farms_for_farmer = sorted(farmer_farms.get(farmer_id, []), key=lambda item: (-item[1], item[0].casefold()))
                farm_summary = ", ".join(f"{farm_name} {farm_loss:,.2f} kg" for farm_name, farm_loss in farms_for_farmer)
                highest_season = max(farmer_seasons.get(farmer_id, {}).items(), key=lambda item: item[1])[0] if farmer_seasons.get(farmer_id) else "no season data"
                farmer_summaries.append(
                    f"#{rank} {name}: {total:,.2f} kg; mainly {main_reason}; highest season {highest_season}; "
                    f"farms [{farm_summary or 'no farm loss records'}]"
                )
            insight_lines.append("• Selected farmer comparison (highest to lowest): " + " | ".join(farmer_summaries) + ".")
        else:
            ranked_ids = sorted(farmer_totals,
                                key=lambda fid: (-farmer_totals[fid], farmer_names.get(fid, "").casefold(), fid))
            if ranked_ids:
                top_farmer_id = ranked_ids[0]
                top_farmer_name = farmer_names.get(top_farmer_id, f"Farmer {top_farmer_id}")
                top_farmer_reason = max(farmer_reasons.get(top_farmer_id, {"no linked reason": 0}).items(), key=lambda item: item[1])[0]
                insight_lines.append(
                    f"• Highest-loss farmer: {top_farmer_name} (ID {top_farmer_id}) — "
                    f"{farmer_totals[top_farmer_id]:,.2f} kg, mainly {top_farmer_reason}."
                )
            else:
                insight_lines.append("• Highest-loss farmer: no farmer is linked to the loss records.")
    insight_text = "\n".join(insight_lines)
    tk.Label(insight, text=insight_text, font=("Arial", 11), bg="#F1F8E9", fg="#444444",
             wraplength=1100, justify="left", anchor="w").pack(anchor="w", padx=16, pady=(0, 12))

    prevention = tk.Frame(content, bg="white", bd=1, relief="solid")
    prevention.pack(fill="x", padx=22, pady=(0, 22))
    tk.Label(prevention, text="Prevention Measures", font=("Arial", 14, "bold"),
             bg="white", fg="#1B5E20").pack(anchor="w", padx=16, pady=(12, 8))
    relevant_ids = {int(row[3]) for row in analytics_rows if row[3] is not None}
    if not selected_ids:
        relevant_ids = set(reason_names)
    grouped_measures = {}
    for measure in measures:
        if int(measure[1]) in relevant_ids:
            grouped_measures.setdefault(int(measure[1]), []).append(str(measure[2]))
    for reason_id in sorted(grouped_measures):
        row_frame = tk.Frame(prevention, bg="#E8F5E9")
        row_frame.pack(fill="x", padx=14, pady=4)
        tk.Label(row_frame, text=reason_names.get(reason_id, f"Reason {reason_id}"),
                 font=("Arial", 10, "bold"), bg="#E8F5E9", fg="#2E7D32",
                 width=24, anchor="w").pack(side="left", padx=10, pady=8)
        joined = "   •   ".join(grouped_measures[reason_id])
        tk.Label(row_frame, text=joined, font=("Arial", 10), bg="#E8F5E9", fg="#444444",
                 anchor="w", justify="left", wraplength=850).pack(side="left", fill="x", expand=True, padx=10, pady=8)
    if not grouped_measures:
        tk.Label(prevention, text="No prevention measures match this selection.",
                 bg="white", fg="#555555").pack(anchor="w", padx=16, pady=(0, 14))

#=========================
#LOGIN PAGE
#=========================
def login():
    username = username_entry.get().strip()
    password = password_entry.get()
    if username == "sri@31" and password == "sri@":
        login_window.withdraw()
        open_dashboard()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password", parent=login_window)


def close_application():
    try:
        if connection.is_connected():
            connection.close()
    except Exception:
        pass
    login_window.destroy()


def open_dashboard():
    dashboard = tk.Toplevel(login_window)
    dashboard.title("Crop Loss Analytics System")
    dashboard.geometry("1280x800")
    dashboard.minsize(1000, 650)
    dashboard.configure(bg="#F4F7F2")
    dashboard.protocol("WM_DELETE_WINDOW", close_application)

    sidebar = tk.Frame(dashboard, bg="#1B5E20", width=245)
    sidebar.pack(side="left", fill="y")
    sidebar.pack_propagate(False)
    tk.Label(sidebar, text="🌾 CROP LOSS", font=("Arial", 17, "bold"),
             bg="#1B5E20", fg="white").pack(pady=(28, 5))
    tk.Label(sidebar, text="Analytics System", font=("Arial", 10),
             bg="#1B5E20", fg="#C8E6C9").pack(pady=(0, 20))
    content = tk.Frame(dashboard, bg="#F4F7F2")
    content.pack(side="left", fill="both", expand=True)

    def clear_content():
        for widget in content.winfo_children():
            widget.destroy()

    def show_home():
        clear_content()
        farmers = view_farmers()
        farms = view_farms()
        crops = view_crops()
        losses = view_crop_losses()
        tk.Label(content, text="Dashboard", font=("Arial", 25, "bold"),
                 bg="#F4F7F2", fg="#1B5E20").pack(anchor="w", padx=30, pady=(30, 2))
        tk.Label(content, text="Crop Loss Reason Tracking & Prevention Analytics",
                 font=("Arial", 11), bg="#F4F7F2", fg="#666666").pack(anchor="w", padx=30)
        card_frame = tk.Frame(content, bg="#F4F7F2")
        card_frame.pack(fill="x", padx=25, pady=25)
        for title, value in (("TOTAL FARMERS", len(farmers)), ("TOTAL FARMS", len(farms)),
                             ("TOTAL CROPS", len(crops)), ("LOSS RECORDS", len(losses))):
            card = tk.Frame(card_frame, bg="white", bd=1, relief="solid")
            card.pack(side="left", fill="both", expand=True, padx=7)
            tk.Label(card, text=title, font=("Arial", 10, "bold"), bg="white", fg="#777777").pack(pady=(18, 5))
            tk.Label(card, text=str(value), font=("Arial", 22, "bold"), bg="white", fg="#2E7D32").pack(pady=(0, 18))
        box = tk.Frame(content, bg="white", bd=1, relief="solid")
        box.pack(fill="both", expand=True, padx=32, pady=10)
        tk.Label(box, text="System Overview", font=("Arial", 16, "bold"),
                 bg="white", fg="#1B5E20").pack(anchor="w", padx=25, pady=(25, 8))
        for text in ("Manage farmers, farms, crops and cultivation details.",
                     "Track crop losses and identify major loss reasons.",
                     "Use the Analytics Dashboard to analyse crop loss patterns."):
            tk.Label(box, text=text, font=("Arial", 11), bg="white", fg="#555555").pack(anchor="w", padx=25, pady=4)
    def show_farmer():
        clear_content()
        open_farmer_window(content)

    def show_farm():
        clear_content()
        open_farm_window(content)

    def show_crop():
        clear_content()
        open_crop_window(content)

    def show_cultivation():
        clear_content()
        open_cultivation_window(content)

    def show_crop_loss():
        clear_content()
        open_crop_loss_window(content)

    def show_loss_reason():
        clear_content()
        open_loss_reason_window(content)

    def show_prevention():
        clear_content()
        open_prevention_window(content)

    def show_analytics(farmer_ids=None):
        clear_content()
        open_analytics_window(content, farmer_ids, show_analytics)

    def menu_button(text, command):
        return tk.Button(sidebar, text=text, font=("Arial", 10, "bold"),
                         bg="#2E7D32", fg="white", activebackground="#388E3C",
                         activeforeground="white", relief="flat", cursor="hand2", command=command)

    menu_button("🏠 Home", show_home).pack(fill="x", padx=15, pady=4)
    menu_button("👨‍🌾 Farmer Management", show_farmer).pack(fill="x", padx=15, pady=4)
    menu_button("🏡 Farm Management", show_farm).pack(fill="x", padx=15, pady=4)
    menu_button("🌱 Crop Management", show_crop).pack(fill="x", padx=15, pady=4)
    menu_button("🌾 Cultivation", show_cultivation).pack(fill="x", padx=15, pady=4)
    menu_button("📉 Crop Loss", show_crop_loss).pack(fill="x", padx=15, pady=4)
    menu_button("⚠ Loss Reasons", show_loss_reason).pack(fill="x", padx=15, pady=4)
    menu_button("🛡 Prevention", show_prevention).pack(fill="x", padx=15, pady=4)
    menu_button("📊 Analytics", show_analytics).pack(fill="x", padx=15, pady=4)
    tk.Button(sidebar, text="↪ Logout", font=("Arial", 10, "bold"), bg="#A93226", fg="white",
              activebackground="#922B21", relief="flat", cursor="hand2",
              command=lambda: logout(dashboard)).pack(side="bottom", fill="x", padx=15, pady=18)
    show_home()


def logout(dashboard):
    if messagebox.askyesno("Logout", "Log out and return to the login screen?", parent=dashboard):
        dashboard.destroy()
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        login_window.deiconify()
        username_entry.focus_set()


def build_login_page():
    global login_window, username_entry, password_entry
    login_window = tk.Tk()
    login_window.title("Login - Crop Loss Analytics")
    login_window.geometry("960x620")
    login_window.minsize(800, 540)
    login_window.configure(bg="#F4F7F2")
    login_window.protocol("WM_DELETE_WINDOW", close_application)

    shell = tk.Frame(login_window, bg="#F4F7F2")
    shell.pack(fill="both", expand=True, padx=30, pady=30)
    brand = tk.Frame(shell, bg="#1B5E20", width=390)
    brand.pack(side="left", fill="both")
    brand.pack_propagate(False)
    tk.Label(brand, text="🌾", font=("Segoe UI Emoji", 64), bg="#1B5E20", fg="white").pack(pady=(78, 10))
    tk.Label(brand, text="CROP LOSS", font=("Arial", 25, "bold"), bg="#1B5E20", fg="white").pack()
    tk.Label(brand, text="ANALYTICS SYSTEM", font=("Arial", 13, "bold"), bg="#1B5E20", fg="#C8E6C9").pack(pady=(4, 24))
    tk.Label(brand, text="Understand crop losses.\nProtect every harvest.",
             font=("Arial", 14), bg="#1B5E20", fg="white", justify="center").pack(pady=8)
    tk.Label(brand, text="Farm • Crop • Season • Prevention", font=("Arial", 10),
             bg="#1B5E20", fg="#DCEFD9").pack(side="bottom", pady=26)

    panel = tk.Frame(shell, bg="white", padx=48, pady=38)
    panel.pack(side="left", fill="both", expand=True)
    tk.Label(panel, text="Welcome back", font=("Arial", 25, "bold"),
             bg="white", fg="#1B5E20").pack(anchor="w", pady=(50, 4))
    tk.Label(panel, text="Sign in to view your farm analytics dashboard.",
             font=("Arial", 11), bg="white", fg="#66736A").pack(anchor="w", pady=(0, 28))
    tk.Label(panel, text="USERNAME", font=("Arial", 9, "bold"), bg="white", fg="#425446").pack(anchor="w", pady=(8, 6))
    username_entry = tk.Entry(panel, font=("Arial", 12), relief="solid", bd=1)
    username_entry.pack(fill="x", ipady=9)
    tk.Label(panel, text="PASSWORD", font=("Arial", 9, "bold"), bg="white", fg="#425446").pack(anchor="w", pady=(18, 6))
    password_entry = tk.Entry(panel, font=("Arial", 12), show="•", relief="solid", bd=1)
    password_entry.pack(fill="x", ipady=9)
    tk.Button(panel, text="SIGN IN  →", font=("Arial", 11, "bold"), bg="#2E7D32", fg="white",
              activebackground="#1B5E20", activeforeground="white", relief="flat", cursor="hand2",
              command=login).pack(fill="x", pady=(28, 12), ipady=10)
    tk.Label(panel, text="Crop Loss Analytics System", font=("Arial", 9),
             bg="white", fg="#8A978C").pack(pady=(16, 0))
    password_entry.bind("<Return>", lambda _event: login())
    username_entry.focus_set()
    return login_window


login_window = build_login_page()
login_window.mainloop()
try:
    if connection.is_connected():
        connection.close()
except Exception:
    pass



