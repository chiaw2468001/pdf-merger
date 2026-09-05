"""
完整使用示例
演示如何使用pdf_merger模組合併多個PDF文件
"""

from pdf_merger import merge_pdfs_with_fallback, merge_pdfs_modern, merge_pdfs_legacy
from pathlib import Path

# ============================================================================
# 範例1: 基本用法（推薦）
# ============================================================================

def example_basic():
    """基本的PDF合併範例"""
    pdf_files = [
        "report_part1.pdf",
        "report_part2.pdf",
        "report_part3.pdf"
    ]
    
    output_file = "complete_report.pdf"
    
    # 使用自動回退方法
    merge_pdfs_with_fallback(pdf_files, output_file)

# ============================================================================
# 範例2: 使用Path物件
# ============================================================================

def example_with_paths():
    """使用pathlib.Path的範例"""
    pdf_dir = Path("./pdfs")
    
    pdf_files = [
        pdf_dir / "chapter1.pdf",
        pdf_dir / "chapter2.pdf",
        pdf_dir / "chapter3.pdf"
    ]
    
    output_file = "book.pdf"
    
    merge_pdfs_with_fallback(pdf_files, output_file)

# ============================================================================
# 範例3: 動態收集PDF檔案
# ============================================================================

def example_dynamic_collection():
    """動態收集目錄中的PDF檔案"""
    pdf_dir = Path("./documents")
    
    # 收集所有PDF檔案（按名稱排序）
    pdf_files = sorted(pdf_dir.glob("*.pdf"))
    
    if not pdf_files:
        print("❌ 沒有找到PDF檔案")
        return
    
    print(f"找到 {len(pdf_files)} 個PDF檔案")
    for pdf_file in pdf_files:
        print(f"  - {pdf_file.name}")
    
    output_file = pdf_dir / "merged_all.pdf"
    
    merge_pdfs_with_fallback(pdf_files, str(output_file))

# ============================================================================
# 範例4: 錯誤處理
# ============================================================================

def example_with_error_handling():
    """包含錯誤處理的範例"""
    pdf_files = [
        "file1.pdf",
        "file2.pdf",
        "file3.pdf"
    ]
    
    output_file = "output.pdf"
    
    try:
        merge_pdfs_with_fallback(pdf_files, output_file)
        print(f"✓ 成功合併PDF到: {output_file}")
    
    except FileNotFoundError as e:
        print(f"❌ 找不到檔案: {e}")
    
    except PermissionError as e:
        print(f"❌ 權限不足: {e}")
    
    except Exception as e:
        print(f"❌ 發生錯誤: {e}")

# ============================================================================
# 範例5: 大量PDF合併
# ============================================================================

def example_batch_merge():
    """批量合併多個PDF組"""
    # 定義多個PDF組
    batch_configs = [
        {
            "name": "Q1報告",
            "files": ["q1_january.pdf", "q1_february.pdf", "q1_march.pdf"],
            "output": "q1_report.pdf"
        },
        {
            "name": "Q2報告",
            "files": ["q2_april.pdf", "q2_may.pdf", "q2_june.pdf"],
            "output": "q2_report.pdf"
        },
        {
            "name": "年度報告",
            "files": ["q1_report.pdf", "q2_report.pdf"],
            "output": "annual_report.pdf"
        }
    ]
    
    for config in batch_configs:
        print(f"\n正在合併: {config['name']}")
        try:
            merge_pdfs_with_fallback(config["files"], config["output"])
        except Exception as e:
            print(f"  ❌ 失敗: {e}")

# ============================================================================
# 主程式
# ============================================================================

if __name__ == "__main__":
    print("PDF合併完整範例\n" + "="*50)
    
    # 取消註釋以運行範例
    # example_basic()
    # example_with_paths()
    # example_dynamic_collection()
    # example_with_error_handling()
    # example_batch_merge()
    
    print("\n請根據您的需求選擇相應的範例函數")
