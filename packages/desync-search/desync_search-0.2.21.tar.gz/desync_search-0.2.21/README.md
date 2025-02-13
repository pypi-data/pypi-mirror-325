

## 1. Installation & Setup

### Installing for the First Time
```bash
pip install desync_search
```

### Updating to the Latest Version
```bash
pip install --upgrade desync_search
```

Make sure you have a valid **Desync Search API key**. You can set it as an environment variable (for example, `DESYNC_API_KEY`) or store it securely in your application’s configuration.

---

## 2. Initializing the DesyncClient

Once you have your API key, you can start using the client. By default, the client points to the production environment. If you want to activate “developer mode” (for example, to use a test endpoint), you can set `developer_mode=True` in the constructor.

**Example:**
```python
from desync_search import DesyncClient
import os

# Fetch your Desync Search API key from an environment variable
my_api_key = os.getenv("DESYNC_API_KEY")

# Initialize the client (production environment by default)
client = DesyncClient(user_api_key=my_api_key)

# Or, to use the developer mode (test environment)
# client = DesyncClient(user_api_key=my_api_key, developer_mode=True)
```

---

## 3. Understanding the PageData Object

Almost all Desync Search actions return or work with an instance of `PageData`. This data structure represents a single search result (i.e., a “page record”). It includes fields such as:

- **`id`**: The internal identifier of the record.
- **`url`**: The page’s URL.
- **`domain`**: The domain portion of the URL.
- **`timestamp`**: When the page was collected.
- **`bulk_search_id`**: If this record was part of a bulk/crawl operation.
- **`search_type`**: e.g., `"stealth_search"` or `"test_search"`.
- **`text_content`**: Extracted text from the page.
- **`html_content`**: Full HTML (if requested).
- **`internal_links`**: List of links on this page pointing to the same domain.
- **`external_links`**: List of links pointing to external domains.
- **`latency_ms`**: How many milliseconds the scraping took (if available).
- **`complete`**: A boolean indicating whether the page’s scraping is fully complete.
- **`created_at`**: The timestamp of record creation in the system.

When you call methods like `search()`, `bulk_search()`, or `crawl()`, the returned values are typically `PageData` instances. You can inspect those instances to analyze URLs, retrieve text content, check completion status, and more.

---

> **Note:** In code, you might see it as:
> ```python
> result_page = client.search("https://example.com")
> print(result_page.url)
> print(result_page.text_content)
> ```
> Each `PageData` object can be handled or stored as needed in your application.


---

## 4. Performing a Single Search

To perform a simple search on a single URL, you can use the `search()` method. This executes a stealth search by default (10 credits per URL). If you want a cheaper test operation (1 credit), set `search_type="test_search"`.

**Example:**
```python
from desync_search import DesyncClient
import os

my_api_key = os.getenv("DESYNC_API_KEY")
client = DesyncClient(my_api_key)

target_url = "https://example.com"
result = client.search(target_url)

# Inspect PageData fields
print("URL:", result.url)
print("Number of internal links:", len(result.internal_links))
print("Number of external links:", len(result.external_links))
print("Text content length:", len(result.text_content))
```

**Available Parameters:**
- **`url`** *(required)*: The target URL to scrape.
- **`search_type`** *(optional)*: `"stealth_search"` (default) or `"test_search"`.
- **`scrape_full_html`** *(optional)*: If `True`, returns full HTML in `html_content`. Default is `False`.
- **`remove_link_duplicates`** *(optional)*: If `True`, deduplicates discovered links. Default is `True`.

The method returns a `PageData` object with fields like `url`, `html_content`, `text_content`, `internal_links`, etc.

---

## 5. Crawling an Entire Domain

For a more powerful operation that follows links recursively within a single domain, use the `crawl()` method. By default, it goes up to `max_depth=2` levels. You can adjust it to go deeper, but be mindful of increased credits usage.

Under the hood, `crawl()`:
1. Performs a single stealth search on the starting URL.
2. Collects all same-domain links.
3. Performs a bulk search on those links, waits for them to complete, and gathers new links at each depth level.
4. Returns a list of `PageData` objects for all discovered pages.

**Example:**
```python
from desync_search import DesyncClient
import os

my_api_key = os.getenv("DESYNC_API_KEY")
client = DesyncClient(user_api_key=my_api_key)

# Crawl up to 3 levels deep on the same domain
all_pages = client.crawl(
    start_url="https://www.example.com",
    max_depth=3,
    scrape_full_html=False,     # Set True if you need HTML content
    remove_link_duplicates=True # Avoid repeated links
)

print(f"Discovered {len(all_pages)} unique pages")

for page in all_pages:
    print("URL:", page.url, "| Depth:", getattr(page, "depth", None))
```

**Parameters Explained:**
- **`start_url`** *(required)*: The initial URL to begin crawling from.
- **`max_depth`** *(optional)*: Maximum link depth to follow (default `2`).
- **`scrape_full_html`** *(optional)*: If `True`, includes the full HTML for each page (`html_content`). Default is `False`.
- **`remove_link_duplicates`** *(optional)*: If `True`, duplicates are filtered out during the search. Default is `True`.
- **`poll_interval`** *(optional)*: How many seconds to wait between checks for bulk-search completion at each depth. Default is `2.0`.
- **`wait_time_per_depth`** *(optional)*: How many seconds to wait for each depth’s bulk operation to complete. Default is `30.0`.
- **`completion_fraction`** *(optional)*: Fraction of links that need to be completed before moving on. Default is `0.975` (97.5%).

`crawl()` returns a list of `PageData` objects, each representing a crawled page. You can inspect their `.depth`, `.url`, `.text_content`, etc., or store them for further analysis.

---

## 6. Bulk Search

If you have a list of URLs to process at once, use `bulk_search()`. Under the hood, this triggers an asynchronous workflow in the Desync system that processes all URLs in parallel. Each URL consumes 10 credits (for stealth search).

### 6.1 Initiating a Bulk Search

```python
from desync_search import DesyncClient
import os

my_api_key = os.getenv("DESYNC_API_KEY")
client = DesyncClient(my_api_key)

# A list of URLs to search
target_list = [
    "https://example.com",
    "https://another-example.net",
    # ... up to 1000
]

# Initiate the bulk search
bulk_info = client.bulk_search(target_list=target_list, extract_html=False)

print("Message:", bulk_info.get("message"))
print("Bulk Search ID:", bulk_info.get("bulk_search_id"))
print("Total links scheduled:", bulk_info.get("total_links"))
print("Cost charged:", bulk_info.get("cost_charged"))
```

#### Returned Fields in `bulk_info`
- **`message`**: Typically `"Bulk search triggered successfully."`.
- **`bulk_search_id`**: A unique ID that identifies this bulk operation.
- **`total_links`**: Number of URLs submitted.
- **`cost_charged`**: Total credits consumed (10 credits per URL).
- **`execution_arn`**: (If applicable) ARN from the underlying AWS Step Functions workflow.

> **Note**: By default, `extract_html=False` excludes the full HTML content from each page to save bandwidth. Set `extract_html=True` if you need HTML in the results.

### 6.2 Retrieving Bulk Search Results

After starting a bulk search, you typically want to wait until it completes before pulling the data. There are two main approaches:

#### (A) Manual Polling and Retrieval

1. **Poll** for minimal info using `list_available`:
   ```python
   partial_records = client.list_available(bulk_search_id=bulk_info["bulk_search_id"])
   ```
   Each item in `partial_records` is a `PageData` with limited fields (e.g., IDs, domains, timestamps, `complete` status).

2. **Check** how many are `complete`:
   ```python
   num_complete = sum(1 for rec in partial_records if rec.complete)
   print(f"{num_complete}/{bulk_info['total_links']} are done.")
   ```

3. **Pull** full data once enough have completed using `pull_data`:
   ```python
   full_records = client.pull_data(bulk_search_id=bulk_info["bulk_search_id"])
   ```
   The resulting list contains `PageData` objects, including fields like `text_content` and `html_content` (if requested).

You can repeat steps 1 & 2 until the desired fraction of pages is complete or until you reach a certain timeout, then proceed with step 3.

#### (B) Automatic Polling with `collect_results`

For convenience, `collect_results` automates the polling loop and retrieves full data once a certain fraction of pages is done or a timeout has passed.

```python
bulk_search_id = bulk_info["bulk_search_id"]
all_results = client.collect_results(
    bulk_search_id=bulk_search_id,
    target_links=target_list,
    wait_time=30.0,        # Max wait time in seconds (default 30s)
    poll_interval=2.0,     # Frequency to check completion (default 2s)
    completion_fraction=0.975  # Fraction of links that must be complete (default 0.975)
)

print(f"Retrieved {len(all_results)} pages.")
for record in all_results:
    print("URL:", record.url, "| Complete:", record.complete)
```

- **`bulk_search_id`**: The ID returned from `bulk_search()`.
- **`target_links`**: The same list passed to `bulk_search`, used for completion calculations.
- **`wait_time`**: Maximum wait time before pulling data regardless.
- **`poll_interval`**: How often to re-check completion status.
- **`completion_fraction`**: Automatically stops polling once this fraction of pages is completed.

Either method will ultimately yield a list of `PageData` objects with their full content (assuming you used `extract_html=True` or if you only need text-based data).

---

**When to Use Bulk Search**  
- **Pros**: Processes multiple URLs in parallel, more efficient than calling `search()` repeatedly.
- **Cons**: Requires you to handle asynchronous polling, either manually or via `collect_results`.



---

## 7. Sample Scripts

### 7.1 Using an Explicit API Key

If you have your API key in a variable (e.g., `my_api_key`), you can directly pass it to the `DesyncClient` constructor:

```python
from desync_search import DesyncClient
import os

my_api_key = os.getenv("DESYNC_API_KEY")  # or any other secure way to retrieve it
client = DesyncClient(user_api_key=my_api_key)

crawl_results = client.crawl(
    start_url="https://www.137ventures.com/",
    max_depth=3
)
```

### 7.2 Relying on an Environment Variable Only

`DesyncClient` can also read the `DESYNC_API_KEY` environment variable automatically if you omit the `user_api_key` argument:

```python
from desync_search import DesyncClient

client = DesyncClient()  # Reads DESYNC_API_KEY from your environment

crawl_results = client.crawl(
    start_url="https://www.137ventures.com/",
    max_depth=3
)
```

Make sure you set the environment variable before running your script. For example, on a Unix-based shell:
```bash
export DESYNC_API_KEY="YOUR_API_KEY_HERE"
python your_script.py
```

On Windows (Command Prompt):
```bat
set DESYNC_API_KEY=YOUR_API_KEY_HERE
python your_script.py
```

Either approach will create a `DesyncClient` that you can immediately use to perform crawls, searches, or bulk operations.