################################
# Random ID (to avoid SG duplicate name error)
################################
resource "random_id" "suffix" {
  byte_length = 4
}

################################
# Security Group for FastAPI
################################
resource "aws_security_group" "fastapi_sg" {
  name        = "fastapi-sg-${random_id.suffix.hex}"
  description = "Security group for FastAPI application"

  ingress {
    description = "Allow SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Allow FastAPI"
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "Allow all outbound traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "fastapi-sg"
  }
}

################################
# EC2 Instance
################################
resource "aws_instance" "fastapi_ec2" {
  ami           = "ami-0f5ee92e2d63afc18" # Amazon Linux 2 (ap-south-1)
  instance_type = "t2.micro"
  key_name      = "fastapi-key"

  vpc_security_group_ids = [
    aws_security_group.fastapi_sg.id
  ]

  tags = {
    Name = "fastapi-ec2"
  }
}
