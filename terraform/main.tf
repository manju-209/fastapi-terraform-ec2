resource "aws_security_group" "fastapi_sg" {
  name = "fastapi-sg"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "fastapi_ec2" {
  ami           = "ami-0f5ee92e2d63afc18"   # Amazon Linux 2 (Mumbai)
  instance_type = "t2.micro"
  key_name = "my-key"

  vpc_security_group_ids = [aws_security_group.fastapi_sg.id]

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install python3 git -y

              cd /home/ec2-user
              git clone https://github.com/manju-209/fastapi-terraform-ec2.git
              cd fastapi-terraform-ec2

              pip3 install -r requirements.txt

              nohup uvicorn main:app --host 0.0.0.0 --port 8000 &
              EOF

  tags = {
    Name = "FastAPI-EC2"
  }
}
