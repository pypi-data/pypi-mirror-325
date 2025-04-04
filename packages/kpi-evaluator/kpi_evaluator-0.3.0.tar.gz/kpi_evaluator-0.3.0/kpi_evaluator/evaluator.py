from ollama import Client
import json

class KPIEvaluator:
    def __init__(self,url_api):
        if url_api is None:
            self.client = Client(host='http://172.16.2.229:5050/')
        else:
            self.client = Client(host = url_api)
            
    def load_json(self,file_employee):
        """Đọc file JSON"""
        with open(file_employee, 'r', encoding='utf-8') as f:
            return json.load(f)

    def load_text(self,file_standard):
        """Đọc file văn bản"""
        with open(file_standard, 'r', encoding='utf-8') as f1:
            return f1.read()
        
    def analyze(self, model , employee_data, standard_kpi):
        """
        Phân tích KPI của nhân viên dựa trên dữ liệu đầu vào và tiêu chuẩn KPI.
        """
        json_employee = self.load_json(employee_data)
        text_standard = self.load_text(standard_kpi)

        prompt_system = f"""
        Bạn là **Chuyên gia Đánh giá KPI** với 10 năm kinh nghiệm phân tích hiệu suất nhân sự trong các tập đoàn đa quốc gia.
        Nhiệm vụ của bạn là phân tích chi tiết các chỉ số KPI của nhân viên dựa trên dữ liệu đầu vào và đối chiếu với bộ chỉ tiêu KPI tiêu chuẩn của doanh nghiệp.

        ### Tiêu chuẩn KPI:
        {text_standard}

        ### Yêu cầu:
        - Định lượng từng KPI, so sánh với tiêu chuẩn.
        - Đưa ra đánh giá tổng quan và gợi ý cải thiện.
        """

        prompt_employee = f"Chỉ số của nhân viên: {json_employee}"

        try:
            response = self.client.generate(model=model, system=prompt_system, prompt=prompt_employee)
            return response['response'].strip() if response else "Lỗi: Không có phản hồi từ mô hình."
        except Exception as e:
            return f"Lỗi API: {str(e)}"
