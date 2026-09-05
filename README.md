# PDF Merger 完整解決方案

提供一個完整的Python PDF合併解決方案，支持多個版本的`pypdf`和`PyPDF2`庫。

## 🚀 快速開始

### 安裝依賴

```bash
# 選項1: 使用pypdf（推薦，現代版本）
pip install pypdf

# 或選項2: 使用PyPDF2（傳統版本）
pip install PyPDF2
```

### 基本使用

```python
from pdf_merger import merge_pdfs_with_fallback

pdf_files = [
    "document1.pdf",
    "document2.pdf",
    "document3.pdf"
]

merge_pdfs_with_fallback(pdf_files, "merged_output.pdf")
```

## 📋 功能介紹

### 三種合併方法

#### 1. **自動回退方法**（推薦）✅
```python
from pdf_merger import merge_pdfs_with_fallback

merge_pdfs_with_fallback(pdf_files, "output.pdf")
```
- ✓ 自動嘗試現代方法
- ✓ 失敗時自動回退到傳統方法
- ✓ 最佳相容性

#### 2. 現代方法（pypdf >= 3.0）
```python
from pdf_merger import merge_pdfs_modern

merge_pdfs_modern(pdf_files, "output.pdf")
```
- ✓ 使用最新的pypdf API
- ✓ 最佳性能
- ✓ 需要pypdf >= 3.0

#### 3. 傳統方法（PyPDF2）
```python
from pdf_merger import merge_pdfs_legacy

merge_pdfs_legacy(pdf_files, "output.pdf")
```
- ✓ 使用PyPDF2庫
- ✓ 向後相容
- ✓ 適合舊系統

## 🔧 進階用法

### 使用pathlib.Path
```python
from pathlib import Path
from pdf_merger import merge_pdfs_with_fallback

pdf_dir = Path("./documents")
pdf_files = [
    pdf_dir / "chapter1.pdf",
    pdf_dir / "chapter2.pdf",
    pdf_dir / "chapter3.pdf"
]

merge_pdfs_with_fallback(pdf_files, "book.pdf")
```

### 動態收集PDF檔案
```python
from pathlib import Path
from pdf_merger import merge_pdfs_with_fallback

pdf_dir = Path("./documents")
pdf_files = sorted(pdf_dir.glob("*.pdf"))  # 自動收集所有PDF

merge_pdfs_with_fallback(pdf_files, "merged_all.pdf")
```

### 錯誤處理
```python
from pdf_merger import merge_pdfs_with_fallback

try:
    merge_pdfs_with_fallback(pdf_files, "output.pdf")
    print("✓ 成功合併")
except FileNotFoundError:
    print("❌ 找不到檔案")
except Exception as e:
    print(f"❌ 發生錯誤: {e}")
```

## 📚 完整範例

查看 `example_usage.py` 獲得更多詳細範例：

- 基本用法
- 使用Path物件
- 動態收集檔案
- 錯誤處理
- 批量合併

運行範例：
```bash
python example_usage.py
```

## 🐛 故障排除

### 問題：ImportError: cannot import name 'PdfMerger'

**解決方案：**

1. 升級pypdf：
```bash
pip install --upgrade pypdf
```

2. 或改用PyPDF2：
```bash
pip install PyPDF2
```

3. 使用自動回退方法（會自動選擇可用的庫）

### 問題：ModuleNotFoundError: No module named 'pypdf'

**解決方案：**
```bash
pip install pypdf
```

### 問題：合併後的PDF無法打開

**解決方案：**
- 確保所有輸入PDF檔案有效且可讀
- 檢查輸出路徑是否有寫入權限
- 嘗試使用另一種方法（modern或legacy）

## 📊 版本相容性

| 方法 | pypdf | PyPDF2 | Python |
|------|-------|--------|--------|
| merge_pdfs_modern | ✅ >= 3.0 | ❌ | ✅ 3.7+ |
| merge_pdfs_legacy | ❌ | ✅ >= 3.0 | ✅ 3.7+ |
| merge_pdfs_with_fallback | ✅ >= 3.0 | ✅ >= 3.0 | ✅ 3.7+ |

## 📝 API 參考

### merge_pdfs_with_fallback(pdf_list, output_filename)

**參數：**
- `pdf_list` (List[Union[str, Path]]): PDF檔案路徑列表
- `output_filename` (str): 輸出檔案名稱

**返回值：** None

**異常：**
- `FileNotFoundError`: 檔案不存在
- `PermissionError`: 沒有寫入權限
- `ImportError`: 未安裝必要的庫

### merge_pdfs_modern(pdf_list, output_filename)

使用pypdf >= 3.0進行合併。

### merge_pdfs_legacy(pdf_list, output_filename)

使用PyPDF2進行合併。

## 💡 最佳實踐

1. **優先使用** `merge_pdfs_with_fallback()`
   - 自動選擇最佳方法
   - 最高相容性

2. **安裝推薦依賴**
   - `pip install pypdf`（最新方案）
   - 如有需要再安裝 `PyPDF2`（備用方案）

3. **檢查檔案**
   - 確保PDF檔案有效且可讀
   - 檢查檔案權限

4. **錯誤處理**
   - 總是使用 try-except 捕捉異常
   - 提供有意義的錯誤訊息

## 📄 授權

MIT License

## 👨‍💻 貢獻

歡迎提交Issue和Pull Request！

## 📧 聯繫方式

如有問題或建議，請提交Issue。
