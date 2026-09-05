"""
PDF合併完整解決方案
支持多個版本的pypdf和PyPDF2
"""

from pathlib import Path
from typing import List, Union

def merge_pdfs_modern(pdf_list: List[Union[str, Path]], output_filename: str) -> None:
    """
    使用pypdf >= 3.0的現代方法
    
    Args:
        pdf_list: PDF檔案路徑列表
        output_filename: 輸出檔案名稱
    """
    try:
        from pypdf import PdfWriter
        
        pdf_writer = PdfWriter()
        
        for pdf_file in pdf_list:
            print(f"正在添加: {pdf_file}")
            pdf_writer.append(pdf_file)
        
        with open(output_filename, "wb") as output:
            pdf_writer.write(output)
        
        print(f"✓ PDF已成功合併到: {output_filename}")
        
    except ImportError:
        print("❌ pypdf未安裝，請運行: pip install pypdf")
        raise

def merge_pdfs_legacy(pdf_list: List[Union[str, Path]], output_filename: str) -> None:
    """
    使用PyPDF2的傳統方法（舊版本相容）
    
    Args:
        pdf_list: PDF檔案路徑列表
        output_filename: 輸出檔案名稱
    """
    try:
        from PyPDF2 import PdfMerger
        
        merger = PdfMerger()
        
        for pdf_file in pdf_list:
            print(f"正在添加: {pdf_file}")
            merger.append(str(pdf_file))
        
        merger.write(output_filename)
        merger.close()
        
        print(f"✓ PDF已成功合併到: {output_filename}")
        
    except ImportError:
        print("❌ PyPDF2未安裝，請運行: pip install PyPDF2")
        raise

def merge_pdfs_with_fallback(pdf_list: List[Union[str, Path]], output_filename: str) -> None:
    """
    自動選擇可用的合併方法
    先嘗試現代方法，失敗則回退到傳統方法
    
    Args:
        pdf_list: PDF檔案路徑列表
        output_filename: 輸出檔案名稱
    """
    try:
        # 先嘗試現代方法
        merge_pdfs_modern(pdf_list, output_filename)
    except (ImportError, Exception) as e:
        print(f"現代方法失敗: {e}")
        print("正在嘗試傳統方法...")
        try:
            merge_pdfs_legacy(pdf_list, output_filename)
        except ImportError:
            print("❌ 請安裝pypdf或PyPDF2:")
            print("   pip install pypdf  或  pip install PyPDF2")
            raise

# ============================================================================
# 使用範例
# ============================================================================

if __name__ == "__main__":
    # 定義PDF檔案列表
    pdf_files = [
        "document1.pdf",
        "document2.pdf",
        "document3.pdf"
    ]
    
    output_file = "merged_output.pdf"
    
    # 方法1: 使用自動回退（推薦）
    merge_pdfs_with_fallback(pdf_files, output_file)
    
    # 方法2: 直接使用現代方法
    # merge_pdfs_modern(pdf_files, output_file)
    
    # 方法3: 直接使用傳統方法
    # merge_pdfs_legacy(pdf_files, output_file)
