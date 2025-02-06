import tkinter as tk
from tkinter import filedialog, messagebox
from .converter import convert_to_webp

def launch_gui():
    root = tk.Tk()
    root.title("WebP 이미지 변환기")
    root.geometry("500x250")

    def select_input_folder():
        input_dir = filedialog.askdirectory(title="변환할 이미지 폴더 선택", mustexist=False)
        if input_dir:
            input_entry.delete(0, tk.END)
            input_entry.insert(0, input_dir)

    def select_output_folder():
        output_dir = filedialog.askdirectory(title="변환된 파일 저장 폴더 선택", mustexist=False)
        if output_dir:
            output_entry.delete(0, tk.END)
            output_entry.insert(0, output_dir)

    def start_conversion():
        input_dir = input_entry.get()
        output_dir = output_entry.get() or None
        
        try:
            quality = int(quality_entry.get())
            if not (0 <= quality <= 100):
                raise ValueError
        except ValueError:
            messagebox.showerror("오류", "품질은 0-100 사이의 정수여야 합니다.")
            return
        
        if not input_dir:
            messagebox.showerror("오류", "입력 폴더를 선택해주세요.")
            return
        
        try:
            converted_count, error_count = convert_to_webp(input_dir, output_dir, quality)
            messagebox.showinfo("변환 완료", f"총 {converted_count}개 파일 변환\n오류 {error_count}개 발생")
        
        except Exception as e:
            messagebox.showerror("오류", f"변환 중 오류 발생: {str(e)}")

    # 입력 폴더 선택
    tk.Label(root, text="입력 폴더:").pack(pady=(10,0))
    input_frame = tk.Frame(root)
    input_frame.pack(pady=(0,10))
    input_entry = tk.Entry(input_frame, width=50)
    input_entry.pack(side=tk.LEFT, padx=(0,10))
    tk.Button(input_frame, text="폴더 선택", command=select_input_folder).pack(side=tk.LEFT)

    # 출력 폴더 선택
    tk.Label(root, text="출력 폴더 (선택사항):").pack()
    output_frame = tk.Frame(root)
    output_frame.pack(pady=(0,10))
    output_entry = tk.Entry(output_frame, width=50)
    output_entry.pack(side=tk.LEFT, padx=(0,10))
    tk.Button(output_frame, text="폴더 선택", command=select_output_folder).pack(side=tk.LEFT)

    # 품질 선택
    tk.Label(root, text="변환 품질 (0-100):").pack()
    quality_frame = tk.Frame(root)
    quality_frame.pack(pady=(0,10))
    quality_entry = tk.Entry(quality_frame, width=10)
    quality_entry.insert(0, "100")
    quality_entry.pack(side=tk.LEFT, padx=(0,10))

    # 변환 버튼
    tk.Button(root, text="이미지 변환 시작", command=start_conversion).pack(pady=20)

    root.mainloop()
