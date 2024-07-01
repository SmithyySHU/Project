import os
import csv
from django.core.management.base import BaseCommand
from webreporting.models import Job
from datetime import datetime
import random
import time



def generate_job_description(job):
    templates = [
        (
            f"We are looking for a {job.title.lower()}, "
            f"to join our team at {job.company}. The ideal candidate will be located in {job.city}, "
            f"{job.state}, and will be responsible for various tasks related to {job.category.lower()}. "
            f"This position is {job.hours.lower()} and offers a salary of {job.salary}. Apply by {job.closing_date}. "
            f"We look forward to hearing from you! Our company is committed to fostering an inclusive environment "
            f"where every team member is valued and can thrive. We emphasize continuous learning and professional growth, "
            f"providing ample opportunities for development. Successful candidates will be expected to exhibit strong analytical "
            f"and problem-solving skills, maintain excellent communication with team members and stakeholders, and demonstrate a "
            f"dedication to high-quality work. In this role, you will collaborate closely with cross-functional teams to drive projects "
            f"forward and meet company objectives. Adaptability, innovation, and attention to detail are key attributes we seek in our "
            f"employees. Our competitive benefits package includes health insurance, retirement plans, and paid time off, all designed to "
            f"support your well-being and work-life balance. Join us to make a meaningful impact and advance your career in a dynamic and "
            f"rewarding work environment."
        ),
        (
            f"Exciting opportunity for a {job.title.lower()} at {job.company}! "
            f"Based in {job.city}, {job.state}, the role involves key responsibilities in the field of {job.category.lower()}. "
            f"This {job.hours.lower()} position offers a competitive salary of {job.salary}. "
            f"Submit your application by {job.closing_date} to be considered. At {job.company}, we prioritize creating a workplace "
            f"that values diversity, equity, and inclusion. We strive to create an environment where every team member feels respected "
            f"and empowered. We are looking for individuals who are passionate about their work, eager to contribute to team success, "
            f"and committed to delivering exceptional results. As part of our team, you will have access to ongoing training and development "
            f"opportunities, ensuring you remain at the forefront of industry trends and best practices. Our collaborative culture encourages "
            f"creativity and innovation, providing you with the support and resources needed to excel in your role. We offer a range of benefits "
            f"to support your health, financial stability, and overall well-being. Apply now to join a forward-thinking company where your skills "
            f"and contributions will be recognized and valued."
        ),
        (
            f"{job.company} is seeking a skilled {job.title.lower()} to be part of our team. "
            f"The position is located in {job.city}, {job.state}, and involves duties related to {job.category.lower()}. "
            f"This is a {job.hours.lower()} role with a salary of {job.salary}. "
            f"Applications are open until {job.closing_date}. We eagerly await your application! At {job.company}, we believe in investing "
            f"in our employees' growth and development. We offer comprehensive training programs, mentorship opportunities, and clear career "
            f"pathways to help you achieve your professional goals. Our team culture is built on collaboration, mutual respect, and a shared "
            f"commitment to excellence. We encourage innovation and creativity, providing a supportive environment where your ideas can flourish. "
            f"We offer a competitive compensation package, including benefits such as health insurance, retirement savings plans, and generous "
            f"paid time off. Join us to be part of a team that values your contributions and supports your career advancement. We look forward to "
            f"seeing how you can make a difference at {job.company}."
        ),
        (
            f"Join us at {job.company} as a {job.title.lower()}! "
            f"The successful candidate will work in {job.city}, {job.state}, focusing on {job.category.lower()} tasks. "
            f"This {job.hours.lower()} role offers a salary of {job.salary}. "
            f"Apply by {job.closing_date} to join our dynamic team. "
            f"We are excited to hear from you! At {job.company}, we are dedicated to creating a positive and inclusive workplace where every employee "
            f"feels valued and supported. Our team is composed of talented professionals who are passionate about their work and committed to achieving "
            f"excellence. We provide ongoing training and development opportunities to help you grow in your career and stay ahead in the industry. Our "
            f"comprehensive benefits package includes health and wellness programs, financial planning resources, and work-life balance initiatives to support "
            f"your overall well-being. We believe that a diverse and inclusive workforce is essential to our success, and we strive to create an environment where "
            f"everyone can thrive. Apply today to become part of a team that values your skills and contributions and offers you the opportunity to make a significant impact."
        ),
        (
            f"{job.company} is hiring a {job.title.lower()} in {job.city}, {job.state}. "
            f"Your expertise in {job.category.lower()} will be highly valued. "
            f"This {job.hours.lower()} position comes with a salary of {job.salary}. "
            f"Make sure to apply by {job.closing_date}. "
            f"We can't wait to review your application! At {job.company}, we are committed to creating a supportive and inclusive workplace where everyone "
            f"can succeed. We offer a range of professional development opportunities, including training programs, workshops, and mentoring, to help you build "
            f"your skills and advance your career. Our team values collaboration, innovation, and excellence, and we strive to create an environment where your "
            f"ideas and contributions are recognized and rewarded. Our benefits package includes comprehensive health insurance, retirement plans, and paid time off, "
            f"designed to support your health and well-being. We are looking for individuals who are passionate about their work and eager to make a positive impact. "
            f"Join us to be part of a dynamic and forward-thinking company that values your talents and provides you with the tools and resources you need to succeed."
        ),
        (
            f"Become a {job.title.lower()} at {job.company}! "
            f"We're located in {job.city}, {job.state}, and need someone skilled in {job.category.lower()}. "
            f"This {job.hours.lower()} position offers a salary of {job.salary}. "
            f"Apply by {job.closing_date}. "
            f"We look forward to your application! At {job.company}, we are passionate about fostering a culture of growth, innovation, and collaboration. We believe that "
            f"our employees are our greatest asset, and we are committed to providing them with the resources and support they need to succeed. We offer a comprehensive "
            f"benefits package, including health and wellness programs, retirement savings plans, and generous paid time off. Our team is dedicated to creating a positive and "
            f"inclusive work environment where everyone feels valued and respected. We encourage continuous learning and professional development, providing opportunities for "
            f"you to grow and advance in your career. Join us to be part of a company that values your skills and contributions and offers you the chance to make a meaningful impact."
        ),
        (
            f"{job.company} is on the lookout for a talented {job.title.lower()} to join our team. "
            f"The role is based in {job.city}, {job.state}, and involves {job.category.lower()} responsibilities. "
            f"This is a {job.hours.lower()} position with a salary of {job.salary}. "
            f"Applications are accepted until {job.closing_date}. "
            f"We hope to hear from you soon! At {job.company}, we are dedicated to creating a workplace that values diversity, equity, and inclusion. We strive to create an environment "
            f"where every team member feels respected and empowered. We are looking for individuals who are passionate about their work, eager to contribute to team success, and committed to "
            f"delivering exceptional results. As part of our team, you will have access to ongoing training and development opportunities, ensuring you remain at the forefront of industry trends "
            f"and best practices. Our collaborative culture encourages creativity and innovation, providing you with the support and resources needed to excel in your role. We offer a range of benefits "
            f"to support your health, financial stability, and overall well-being. Apply now to join a forward-thinking company where your skills and contributions will be recognized and valued."
        ),
        (
            f"Opportunity awaits at {job.company} for a {job.title.lower()}! "
            f"Located in {job.city}, {job.state}, this role involves {job.category.lower()} duties. "
            f"This {job.hours.lower()} position comes with a competitive salary of {job.salary}. "
            f"Please apply by {job.closing_date}. "
            f"We look forward to receiving your application! At {job.company}, we prioritize creating a workplace that values diversity, equity, and inclusion. We strive to create an environment "
            f"where every team member feels respected and empowered. We are looking for individuals who are passionate about their work, eager to contribute to team success, and committed to delivering "
            f"exceptional results. As part of our team, you will have access to ongoing training and development opportunities, ensuring you remain at the forefront of industry trends and best practices. "
            f"Our collaborative culture encourages creativity and innovation, providing you with the support and resources needed to excel in your role. We offer a range of benefits to support your health, "
            f"financial stability, and overall well-being. Apply now to join a forward-thinking company where your skills and contributions will be recognized and valued."
        ),
        (
            f"Are you a {job.title.lower()}? {job.company} wants you! "
            f"Our team in {job.city}, {job.state} is looking for someone with {job.category.lower()} skills. "
            f"This {job.hours.lower()} role offers a salary of {job.salary}. "
            f"Apply by {job.closing_date} to join us. "
            f"We're excited to hear from you! At {job.company}, we are dedicated to creating a workplace that values diversity, equity, and inclusion. We strive to create an environment where every team "
            f"member feels respected and empowered. We are looking for individuals who are passionate about their work, eager to contribute to team success, and committed to delivering exceptional results. "
            f"As part of our team, you will have access to ongoing training and development opportunities, ensuring you remain at the forefront of industry trends and best practices. Our collaborative culture "
            f"encourages creativity and innovation, providing you with the support and resources needed to excel in your role. We offer a range of benefits to support your health, financial stability, and overall well-being. "
            f"Apply now to join a forward-thinking company where your skills and contributions will be recognized and valued."
        ),
        (
            f"{job.company} is seeking a {job.title.lower()} for our team in {job.city}, {job.state}. "
            f"Responsibilities include various {job.category.lower()} tasks. "
            f"This {job.hours.lower()} position offers a salary of {job.salary}. "
            f"Submit your application by {job.closing_date}. "
            f"We look forward to your response! At {job.company}, we are dedicated to creating a workplace that values diversity, equity, and inclusion. We strive to create an environment where every team member feels respected and empowered. "
            f"We are looking for individuals who are passionate about their work, eager to contribute to team success, and committed to delivering exceptional results. As part of our team, you will have access to ongoing training and development opportunities, "
            f"ensuring you remain at the forefront of industry trends and best practices. Our collaborative culture encourages creativity and innovation, providing you with the support and resources needed to excel in your role. We offer a range of benefits to support your health, "
            f"financial stability, and overall well-being. Apply now to join a forward-thinking company where your skills and contributions will be recognized and valued."
        ),
        (
            f"Join the {job.company} team as a {job.title.lower()}! "
            f"This role is based in {job.city}, {job.state}, focusing on {job.category.lower()} responsibilities. "
            f"This {job.hours.lower()} position offers a competitive salary of {job.salary}. "
            f"Applications are open until {job.closing_date}. "
            f"We eagerly await your application! At {job.company}, we are dedicated to creating a workplace that values diversity, equity, and inclusion. We strive to create an environment where every team member feels respected and empowered. "
            f"We are looking for individuals who are passionate about their work, eager to contribute to team success, and committed to delivering exceptional results. As part of our team, you will have access to ongoing training and development opportunities, "
            f"ensuring you remain at the forefront of industry trends and best practices. Our collaborative culture encourages creativity and innovation, providing you with the support and resources needed to excel in your role. We offer a range of benefits to support your health, "
            f"financial stability, and overall well-being. Apply now to join a forward-thinking company where your skills and contributions will be recognized and valued."
        )
    ]

    description = random.choice(templates)
    return description
    


class Command(BaseCommand):
    help = 'Import job listings from CSV file'

    def handle(self, *args, **kwargs):
        with open('webreporting/data/cleanedData.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                job, created = Job.objects.get_or_create(
                    title=row['title'],
                    posting_date=datetime.strptime(row['postingDate'], '%Y-%m-%d'),
                    salary=row['salary'],
                    hours=row['hours'],
                    closing_date=datetime.strptime(row['closingDate'], '%Y-%m-%d'),
                    location=row['location'],
                    state=row['state'],
                    city=row['city'],
                    company=row['company'],
                    job_type=row['jobType'],
                    category=row['category'],
                    job_reference=row['jobReference'],
                    additional_salary_info=row.get('additionalSalaryInf', ''),
                    min_salary=row.get('minSalary', None),
                    max_salary=row.get('maxSalary', None),
                    salary_type=row['salaryType'],
                    avg_salary=row.get('avgSalary', None)
                )
                if created:
                    job.job_description = generate_job_description(job)
                    job.save()
                    self.stdout.write(self.style.SUCCESS(f'Successfully added job listing: {job.title}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Job listing {job.title} already exists'))
