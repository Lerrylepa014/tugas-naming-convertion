# Sistem Manajemen Mahasiswa
# Implementasi Naming Convention Python (PEP 8)

class StudentManager:
    """
    Kelas untuk mengelola data mahasiswa
    Menggunakan PascalCase untuk nama kelas
    """
    
    def __init__(self):
        # snake_case untuk variabel dan method
        self.student_list = []
        self.total_students = 0
    
    def add_student(self, student_name, student_id, gpa_score):
        """
        Menambahkan mahasiswa baru ke dalam sistem
        
        Args:
            student_name (str): Nama mahasiswa
            student_id (str): NIM mahasiswa  
            gpa_score (float): IPK mahasiswa
        """
        # Dictionary dengan snake_case keys
        new_student = {
            'name': student_name,
            'id': student_id,
            'gpa': gpa_score,
            'enrollment_status': 'active'
        }
        
        self.student_list.append(new_student)
        self.total_students += 1
        print(f"Mahasiswa {student_name} berhasil ditambahkan!")
    
    def display_all_students(self):
        """Menampilkan semua data mahasiswa"""
        if not self.student_list:
            print("Tidak ada data mahasiswa.")
            return
        
        print("\n=== DAFTAR MAHASISWA ===")
        for index, student in enumerate(self.student_list, 1):
            print(f"{index}. Nama: {student['name']}")
            print(f"   NIM: {student['id']}")
            print(f"   IPK: {student['gpa']}")
            print(f"   Status: {student['enrollment_status']}")
            print("-" * 30)
    
    def find_student_by_id(self, target_student_id):
        """
        Mencari mahasiswa berdasarkan NIM
        
        Args:
            target_student_id (str): NIM yang dicari
            
        Returns:
            dict or None: Data mahasiswa jika ditemukan
        """
        for student in self.student_list:
            if student['id'] == target_student_id:
                return student
        return None
    
    def calculate_average_gpa(self):
        """
        Menghitung rata-rata IPK semua mahasiswa
        
        Returns:
            float: Rata-rata IPK
        """
        if not self.student_list:
            return 0.0
        
        total_gpa = sum(student['gpa'] for student in self.student_list)
        average_gpa = total_gpa / len(self.student_list)
        return round(average_gpa, 2)
    
    def get_honor_students(self, min_gpa_threshold=3.5):
        """
        Mendapatkan daftar mahasiswa berprestasi
        
        Args:
            min_gpa_threshold (float): Batas minimum IPK
            
        Returns:
            list: Daftar mahasiswa berprestasi
        """
        honor_students = [
            student for student in self.student_list 
            if student['gpa'] >= min_gpa_threshold
        ]
        return honor_students


def display_menu():
    """Menampilkan menu pilihan"""
    print("\n=== MENU SISTEM MANAJEMEN MAHASISWA ===")
    print("1. Tambah Mahasiswa")
    print("2. Tampilkan Semua Mahasiswa")
    print("3. Cari Mahasiswa berdasarkan NIM")
    print("4. Tampilkan Rata-rata IPK")
    print("5. Tampilkan Mahasiswa Berprestasi")
    print("6. Keluar")
    print("=" * 40)


def get_valid_gpa():
    """
    Mendapatkan input IPK yang valid dari user
    
    Returns:
        float: IPK yang valid (0.0 - 4.0)
    """
    while True:
        try:
            gpa_input = float(input("Masukkan IPK (0.0 - 4.0): "))
            if 0.0 <= gpa_input <= 4.0:
                return gpa_input
            else:
                print("IPK harus antara 0.0 - 4.0!")
        except ValueError:
            print("Input tidak valid! Masukkan angka desimal.")


def get_student_input():
    """
    Mendapatkan input data mahasiswa dari user
    
    Returns:
        tuple: (nama, nim, ipk)
    """
    print("\n--- INPUT DATA MAHASISWA ---")
    student_name = input("Masukkan nama mahasiswa: ").strip()
    
    while True:
        student_id = input("Masukkan NIM: ").strip()
        if student_id:
            break
        print("NIM tidak boleh kosong!")
    
    student_gpa = get_valid_gpa()
    
    return student_name, student_id, student_gpa


def main():
    """Fungsi utama program"""
    # Konstanta menggunakan UPPER_CASE
    MIN_GPA = 0.0
    MAX_GPA = 4.0
    MENU_EXIT = 6
    
    # Membuat instance dari StudentManager
    student_manager = StudentManager()
    
    print("=== SISTEM MANAJEMEN MAHASISWA ===")
    print("Selamat datang di Sistem Manajemen Mahasiswa!")
    
    while True:
        display_menu()
        
        try:
            user_choice = int(input("Pilih menu (1-6): "))
            
            if user_choice == 1:
                # Tambah mahasiswa
                try:
                    name, nim, gpa = get_student_input()
                    student_manager.add_student(name, nim, gpa)
                except KeyboardInterrupt:
                    print("\nInput dibatalkan.")
                
            elif user_choice == 2:
                # Tampilkan semua mahasiswa
                student_manager.display_all_students()
                
            elif user_choice == 3:
                # Cari mahasiswa berdasarkan NIM
                search_nim = input("\nMasukkan NIM yang dicari: ").strip()
                found_student = student_manager.find_student_by_id(search_nim)
                
                if found_student:
                    print(f"\n--- MAHASISWA DITEMUKAN ---")
                    print(f"Nama: {found_student['name']}")
                    print(f"NIM: {found_student['id']}")
                    print(f"IPK: {found_student['gpa']}")
                    print(f"Status: {found_student['enrollment_status']}")
                else:
                    print(f"Mahasiswa dengan NIM {search_nim} tidak ditemukan.")
                
            elif user_choice == 4:
                # Tampilkan rata-rata IPK
                avg_gpa = student_manager.calculate_average_gpa()
                total_count = len(student_manager.student_list)
                print(f"\n--- STATISTIK IPK ---")
                print(f"Total mahasiswa: {total_count}")
                print(f"Rata-rata IPK: {avg_gpa}")
                
            elif user_choice == 5:
                # Tampilkan mahasiswa berprestasi
                try:
                    min_threshold = float(input("Masukkan batas minimum IPK (default 3.5): ") or "3.5")
                    honor_students = student_manager.get_honor_students(min_threshold)
                    
                    print(f"\n--- MAHASISWA BERPRESTASI (IPK >= {min_threshold}) ---")
                    if honor_students:
                        print(f"Jumlah: {len(honor_students)} mahasiswa")
                        for i, student in enumerate(honor_students, 1):
                            print(f"{i}. {student['name']} - IPK: {student['gpa']}")
                    else:
                        print(f"Tidak ada mahasiswa dengan IPK >= {min_threshold}")
                        
                except ValueError:
                    print("Input tidak valid! Menggunakan nilai default 3.5")
                    honor_students = student_manager.get_honor_students()
                    print(f"Mahasiswa Berprestasi: {len(honor_students)} orang")
                
            elif user_choice == MENU_EXIT:
                # Keluar dari program
                print("\nTerima kasih telah menggunakan Sistem Manajemen Mahasiswa!")
                break
                
            else:
                print("Pilihan tidak valid! Silakan pilih menu 1-6.")
                
        except ValueError:
            print("Input tidak valid! Masukkan angka 1-6.")
        except KeyboardInterrupt:
            print("\n\nProgram dihentikan oleh user.")
            break
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
        
        # Pause sebelum kembali ke menu
        input("\nTekan Enter untuk melanjutkan...")
        print("\n" + "="*50)


if __name__ == "__main__":
    main()