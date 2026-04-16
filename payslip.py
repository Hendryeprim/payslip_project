from fpdf import FPDF
import datetime

def create_pdf_payslip(emp_id, emp_name, basic, allowances, deductions):
    # Calculate salaries
    gross = basic + allowances
    net = gross - deductions
    date_today = datetime.date.today().strftime("%Y-%m-%d")

    # Initialize PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Header
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="COMPANY XYZ - OFFICIAL PAYSLIP", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Date: {date_today}", ln=True, align='C')
    pdf.line(10, 30, 200, 30) # Draw a line
    pdf.ln(10) # Add a blank line

    # Employee Details
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(50, 10, txt="Employee ID:")
    pdf.set_font("Arial", size=12)
    pdf.cell(50, 10, txt=emp_id, ln=True)

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(50, 10, txt="Employee Name:")
    pdf.set_font("Arial", size=12)
    pdf.cell(50, 10, txt=emp_name, ln=True)
    pdf.ln(10)

    # Salary Details
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(100, 10, txt="Earnings", border=1)
    pdf.cell(90, 10, txt="Amount ($)", border=1, ln=True, align='R')
    
    pdf.set_font("Arial", size=12)
    pdf.cell(100, 10, txt="Basic Salary", border=1)
    pdf.cell(90, 10, txt=f"{basic:,.2f}", border=1, ln=True, align='R')
    
    pdf.cell(100, 10, txt="Allowances", border=1)
    pdf.cell(90, 10, txt=f"{allowances:,.2f}", border=1, ln=True, align='R')

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(100, 10, txt="Gross Salary", border=1)
    pdf.cell(90, 10, txt=f"{gross:,.2f}", border=1, ln=True, align='R')

    # Deductions
    pdf.ln(5)
    pdf.cell(100, 10, txt="Deductions", border=1)
    pdf.cell(90, 10, txt="Amount ($)", border=1, ln=True, align='R')
    
    pdf.set_font("Arial", size=12)
    pdf.cell(100, 10, txt="Tax / Others", border=1)
    pdf.cell(90, 10, txt=f"-{deductions:,.2f}", border=1, ln=True, align='R')

    # Net Salary
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(100, 15, txt="NET SALARY", border=1)
    pdf.cell(90, 15, txt=f"${net:,.2f}", border=1, ln=True, align='R')

    # Save the PDF
    filename = f"Payslip_{emp_id}_{date_today}.pdf"
    pdf.output(filename)
    print(f"Successfully generated PDF: {filename}")

# Run the program
if __name__ == "__main__":
    print("--- PDF Payslip Generator ---")
    emp_id = input("Enter Employee ID: ")
    emp_name = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))
    allow = float(input("Enter Allowances: "))
    deduct = float(input("Enter Deductions: "))
    
    create_pdf_payslip(emp_id, emp_name, basic, allow, deduct)
    