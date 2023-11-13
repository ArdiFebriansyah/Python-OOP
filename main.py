class CTitik():
    def __init__(self):
        print("\nSelamat Datang Di Program Penambahan Koordinat")
        print("_______________________________________________\n")

    def coordinate(self):
        x = input("Enter The First Coordinate (x): ")
        y = input("Enter The Second Coordinate(y): ")

        self.x = []

        self.x.append(x)
        self.x.append(y)

        x2 = input("Enter The First Coordinate (x): ")
        y2 = input("Enter The Second Coordinate (y): ")

        self.x2 = []

        self.x2.append(x2)
        self.x2.append(y2)


    def sum(self):
       total = []
       hasil1 = int(self.x[0]) + int(self.x2[0])
       hasil2 = int(self.x[1]) + int(self.x2[1])

       total.append(hasil1)
       total.append(hasil2)

       print(f"Total = {total}")

titik = CTitik()
titik.coordinate()
titik.sum()
