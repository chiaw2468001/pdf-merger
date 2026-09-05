"""
PDF合併進階方案 - 支持選擇特定頁面
"""

from pathlib import Path
from typing import List, Union, Optional, Dict, Tuple
from pypdf import PdfWriter, PdfReader

# ============================================================================
# 進階功能1: 合併特定頁面範圍
# ============================================================================

def merge_pdfs_page_range(
    pdf_list: List[Union[str, Path]], 
    output_filename: str,
    page_ranges: Optional[Dict[str, Tuple[int, int]]] = None
) -> None:
    """
    合併PDF的特定頁面範圍
    
    Args:
        pdf_list: PDF檔案路徑列表
        output_filename: 輸出檔案名稱
        page_ranges: 頁面範圍字典
                    格式: {"file1.pdf": (0, 5), "file2.pdf": (2, 8)}
                    表示: file1.pdf的第0-5頁，file2.pdf的第2-8頁
                    如果為None，則使用所有頁面
    
    範例:
        pdf_list = ["doc1.pdf", "doc2.pdf", "doc3.pdf"]
        ranges = {
            "doc1.pdf": (0, 3),      # 第1-4頁
            "doc2.pdf": (1, 5),      # 第2-6頁
            "doc3.pdf": (0, 2)       # 第1-3頁
        }
        merge_pdfs_page_range(pdf_list, "output.pdf", ranges)
    """
    writer = PdfWriter()
    
    for pdf_file in pdf_list:
        pdf_file = str(pdf_file)
        reader = PdfReader(pdf_file)
        
        # 取得頁面範圍
        if page_ranges and pdf_file in page_ranges:
            start, end = page_ranges[pdf_file]
            pages = range(start, min(end + 1, len(reader.pages)))
            print(f"添加 {pdf_file}: 第 {start+1}-{end+1} 頁 (共 {len(reader.pages)} 頁)")
        else:
            pages = range(len(reader.pages))
            print(f"添加 {pdf_file}: 所有 {len(reader.pages)} 頁")
        
        # 添加指定頁面
        for page_num in pages:
            writer.add_page(reader.pages[page_num])\n    with open(output_filename, "wb") as f:
        writer.write(f)
    
    print(f"✅ 成功合併！已保存至: {output_filename}")

# ============================================================================
# 進階功能2: 選擇特定頁碼合併
# ============================================================================

def merge_pdfs_specific_pages(
    pdf_pages: List[Tuple[str, List[int]]],
    output_filename: str
) -> None:
    """
    合併指定PDF檔案的指定頁碼
    
    Args:
        pdf_pages: 列表，每個元素為 (PDF路徑, 頁碼列表)
                  頁碼從0開始
        output_filename: 輸出檔案名稱
    
    範例:
        pdf_pages = [
            ("doc1.pdf", [0, 1, 2]),        # doc1的第1,2,3頁
            ("doc2.pdf", [0, 5, 10]),       # doc2的第1,6,11頁
            ("doc3.pdf", [0, 1, 2, 3])      # doc3的第1,2,3,4頁
        ]
        merge_pdfs_specific_pages(pdf_pages, "output.pdf")
    """
    writer = PdfWriter()
    
    for pdf_file, page_numbers in pdf_pages:
        pdf_file = str(pdf_file)
        reader = PdfReader(pdf_file)
        
        print(f"處理 {pdf_file}:")
        
        for page_num in page_numbers:
            if 0 <= page_num < len(reader.pages):
                writer.add_page(reader.pages[page_num])
                print(f"  ✓ 添加第 {page_num + 1} 頁")
            else:
                print(f"  ✗ 警告: 頁碼 {page_num + 1} 超出範圍 (共 {len(reader.pages)} 頁)")
    
    with open(output_filename, "wb") as f:
        writer.write(f)
    
    print(f"\n✅ 成功合併！已保存至: {output_filename}")

# ============================================================================
# 進階功能3: 交錯合併（如掃描的雙面文件）
# ============================================================================

def merge_pdfs_interleave(
    odd_pdf: Union[str, Path],
    even_pdf: Union[str, Path],
    output_filename: str
) -> None:
    """
    交錯合併兩個PDF（用於雙面掃描文件）
    
    Args:
        odd_pdf: 奇數頁PDF路徑
        even_pdf: 偶數頁PDF路徑
        output_filename: 輸出檔案名稱
    
    範例:
        merge_pdfs_interleave("odd_pages.pdf", "even_pages.pdf", "complete.pdf")
        # 結果: 奇數頁1, 偶數頁1, 奇數頁2, 偶數頁2, ...
    """
    reader_odd = PdfReader(str(odd_pdf))
    reader_even = PdfReader(str(even_pdf))
    writer = PdfWriter()
    
    max_pages = max(len(reader_odd.pages), len(reader_even.pages))
    
    print(f"奇數頁PDF: {len(reader_odd.pages)} 頁")
    print(f"偶數頁PDF: {len(reader_even.pages)} 頁")
    print(f"開始交錯合併...")
    
    for i in range(max_pages):
        if i < len(reader_odd.pages):
            writer.add_page(reader_odd.pages[i])
            print(f"✓ 添加奇數頁 {i+1}")
        
        if i < len(reader_even.pages):
            writer.add_page(reader_even.pages[i])
            print(f"✓ 添加偶數頁 {i+1}")
    
    with open(output_filename, "wb") as f:
        writer.write(f)
    
    print(f"\n✅ 成功合併！已保存至: {output_filename}")

# ============================================================================
# 進階功能4: 顯示PDF頁數資訊
# ============================================================================

def show_pdf_info(pdf_list: List[Union[str, Path]]) -> None:
    """
    顯示PDF檔案的頁數資訊
    
    Args:
        pdf_list: PDF檔案路徑列表
    
    範例:
        show_pdf_info(["doc1.pdf", "doc2.pdf", "doc3.pdf"])
    """
    print("📄 PDF檔案資訊:")
    print("-" * 50)
    
    total_pages = 0
    
    for pdf_file in pdf_list:
        pdf_file = str(pdf_file)
        try:
            reader = PdfReader(pdf_file)
            num_pages = len(reader.pages)
            total_pages += num_pages
            print(f"{pdf_file}: {num_pages} 頁")
        except Exception as e:
            print(f"{pdf_file}: ✗ 讀取失敗 ({e})")
    
    print("-" * 50)
    print(f"總頁數: {total_pages} 頁")

# ============================================================================
# 進階功能5: 智能分割PDF（根據頁數）
# ============================================================================

def split_pdf_by_count(
    pdf_file: Union[str, Path],
    pages_per_file: int,
    output_dir: str = "./"
) -> List[str]:
    """
    將PDF按指定頁數分割成多個檔案
    
    Args:
        pdf_file: 要分割的PDF路徑
        pages_per_file: 每個檔案包含的頁數
        output_dir: 輸出目錄
    
    返回:
        輸出檔案路徑列表
    
    範例:
        output_files = split_pdf_by_count("large_document.pdf", 10)
        # 會生成: large_document_part1.pdf, large_document_part2.pdf, ...
    """
    pdf_file = Path(pdf_file)
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)
    
    reader = PdfReader(str(pdf_file))
    total_pages = len(reader.pages)
    
    print(f"分割 {pdf_file} (共 {total_pages} 頁)")
    print(f"每個檔案: {pages_per_file} 頁")
    
    output_files = []
    part_num = 1
    
    for start_page in range(0, total_pages, pages_per_file):
        end_page = min(start_page + pages_per_file, total_pages)
        
        writer = PdfWriter()
        
        for page_num in range(start_page, end_page):
            writer.add_page(reader.pages[page_num])
        
        # 生成輸出檔案名稱
        stem = pdf_file.stem
        suffix = pdf_file.suffix
        output_file = output_dir / f"{stem}_part{part_num}{suffix}"
        
        with open(output_file, "wb") as f:
            writer.write(f)
        
        output_files.append(str(output_file))
        print(f"✓ 生成: {output_file.name} (第 {start_page+1}-{end_page} 頁)")
        
        part_num += 1
    
    print(f"\n✅ 分割完成！生成 {len(output_files)} 個檔案")
    return output_files

# ============================================================================
# 進階功能6: 旋轉頁面
# ============================================================================

def merge_pdfs_with_rotation(
    pdf_list: List[Union[str, Path]],
    output_filename: str,
    rotation_map: Optional[Dict[str, int]] = None
) -> None:
    """
    合併PDF並支持旋轉指定頁面
    
    Args:
        pdf_list: PDF檔案路徑列表
        output_filename: 輸出檔案名稱
        rotation_map: 旋轉角度字典，格式: {"file.pdf": 90}
                     支持的角度: 0, 90, 180, 270
    
    範例:
        rotation_map = {"doc1.pdf": 90, "doc2.pdf": 180}
        merge_pdfs_with_rotation(
            ["doc1.pdf", "doc2.pdf"],
            "output.pdf",
            rotation_map
        )
    """
    writer = PdfWriter()
    
    for pdf_file in pdf_list:
        pdf_file = str(pdf_file)
        reader = PdfReader(pdf_file)
        rotation = rotation_map.get(pdf_file, 0) if rotation_map else 0
        
        print(f"添加 {pdf_file} (旋轉 {rotation}°)")
        
        for page in reader.pages:
            if rotation != 0:
                page.rotate(rotation)
            writer.add_page(page)
    
    with open(output_filename, "wb") as f:
        writer.write(f)
    
    print(f"✅ 成功合併！已保存至: {output_filename}")

# ============================================================================
# 使用範例
# ============================================================================

if __name__ == "__main__":
    print("PDF合併進階方案 - 範例演示\n" + "="*50 + "\n")
    
    # 範例1: 特定頁面範圍合併
    print("📌 範例1: 特定頁面範圍合併")
    pdf_list = ["doc1.pdf", "doc2.pdf", "doc3.pdf"]
    ranges = {
        "doc1.pdf": (0, 3),      # 第1-4頁
        "doc2.pdf": (1, 5),      # 第2-6頁
        "doc3.pdf": (0, 2)       # 第1-3頁
    }
    # merge_pdfs_page_range(pdf_list, "output_ranges.pdf", ranges)
    
    # 範例2: 選擇特定頁碼
    print("\n📌 範例2: 選擇特定頁碼")
    pdf_pages = [
        ("doc1.pdf", [0, 1, 2]),
        ("doc2.pdf", [0, 5, 10]),
        ("doc3.pdf", [0, 1, 2, 3])
    ]
    # merge_pdfs_specific_pages(pdf_pages, "output_specific.pdf")
    
    # 範例3: 顯示PDF資訊
    print("\n📌 範例3: 顯示PDF資訊")
    # show_pdf_info(["doc1.pdf", "doc2.pdf", "doc3.pdf"])
    
    print("\n取消註釋上方代碼即可運行！")
