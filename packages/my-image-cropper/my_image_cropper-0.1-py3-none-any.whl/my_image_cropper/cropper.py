import os
import ctypes
import json
from tkinter import Tk, messagebox
from tkinter.filedialog import askopenfilenames, askopenfilename
from PIL import Image

def main():

    # ポップアップの解像度調整
    ctypes.windll.shcore.SetProcessDpiAwareness(1)

    # Tkinterのルートウィンドウを作成し、非表示にする
    root = Tk()
    root.withdraw()  # メインウィンドウを表示しない

    # スクリプトのディレクトリを取得
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # スクリプトのディレクトリ内のJSONファイルを取得
    json_files = [f for f in os.listdir(script_dir) if f.endswith('.json')]

    # JSONファイルが1つだけの場合、そのファイルを使用
    if len(json_files) == 1:
        json_file_path = os.path.join(script_dir, json_files[0])
    else:
        # JSONファイルが2つ以上ある場合、ユーザーに選択させる
        if json_files:
            json_file_path = askopenfilename(title="JSONファイルを選択", filetypes=[("JSON files", "*.json")], initialdir=script_dir)
            if not json_file_path:  # ユーザーがキャンセルした場合
                messagebox.showinfo("情報", "JSONファイルが選択されませんでした。")
                exit()
        else:
            messagebox.showerror("エラー", "JSONファイルが見つかりませんでした。")
            exit()

    # JSONファイルからトリミング領域を読み込む
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        crop_area = tuple(data['crop_area'])  # トリミング領域をタプルに変換

    # ユーザーにファイルを選択させる
    file_paths = askopenfilenames(title="画像ファイルを選択", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])

    # 選択されたファイルがある場合
    if file_paths:
        # 最初のファイルのパスからディレクトリを取得
        first_image_path = file_paths[0]
        output_folder = os.path.join(os.path.dirname(first_image_path), 'after')  # 'after'フォルダを指定

        # 'after'フォルダが存在しない場合は作成
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # 選択されたファイルに対して処理を行う
        for image_path in file_paths:
            try:
                # 画像を開く
                image = Image.open(image_path)
                
                # 画像のサイズを取得
                width, height = image.size
                
                # トリミング領域が画像のサイズを超えないか確認
                if (crop_area[0] < 0 or crop_area[1] < 0 or 
                    crop_area[2] > width or crop_area[3] > height):
                    print(f"トリミング領域が画像のサイズを超えています: {os.path.basename(image_path)}")
                    continue
                
                # 画像をトリミング
                cropped_image = image.crop(crop_area)
                
                # トリミングした画像を保存 (output_folderに保存)
                cropped_image_path = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(image_path))[0]}_cropped{os.path.splitext(image_path)[1]}")
                cropped_image.save(cropped_image_path)

                print(f"トリミングした画像を保存しました: {cropped_image_path}")
            
            except Exception as e:
                print(f"画像処理中にエラーが発生しました: {os.path.basename(image_path)} - {e}")
    else:
        print("画像ファイルが選択されませんでした。")

if __name__ == "__main__":
    main()