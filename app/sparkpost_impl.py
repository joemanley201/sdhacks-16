from sparkpost import SparkPost
sp = SparkPost('89ade4b086761273ffc0ab5fca6b4acde6f0d6a0')

def send_email(recipient, other_members):
	response = sp.transmissions.send(
	    recipients=[recipient],
	    html = '<p>Hey there</p>' + 'We have formed a Caboodle for you and your other members are: ' + ", ".join(other_members) + "<p>Have fun</p><br><p>Sent by SparkPost</p>",
	    from_email='postmaster@go-caboodle.com',
	    reply_to='postmaster@go-caboodle.com',
	    subject='Hey there, welcome!'
    )