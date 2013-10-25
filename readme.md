# Stack Exchange Trends Website

This web application allows to explore trends based on [Stack Exchange network](http://stackexchange.com/) tags, and see various visualizations to reveal cool new insights regarding the tags and the posts attached to them.

![alt text](https://github.com/alexeyza/stackexchange-trends/raw/master/screenshot.jpg "Stack Exchange Trends Screenshot")

## How to Use
Follow these steps:

1. Download the source code from GitHub.
2. Download the Stack Exchange dump file ([link](http://www.clearbits.net/creators/146-stack-exchange-data-dump))
3. Copy the XML files of the domain of your choice (i.e. Stack Overflow files) to the same directory as the source code.
4. Run `python create_se_db.py` to create an SQLite3 database with the required data. It should create a `bigdata.db` file.
5. Run `python se_trends.py` to run the web server locally (availible at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)). Or use a remote server to run the application (make sure it supports [Flask](http://flask.pocoo.org/) and [SQLite3](http://www.sqlite.org/)).

## Beta
This web application is in early development and may not work properly (or at all). Its design is still under development (I'm open to suggestions).

---
Copyright (C) 2013 Alexey Zagalsky

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.