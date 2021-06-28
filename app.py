from flask import Flask, render_template, request


Score_alphabet =0
BScore_alphabet =0

app = Flask(__name__,template_folder="templates")

@app.route('/')
def home():
	return render_template('number.html')


import guessing_number
@app.route('/send', methods=['GET', 'POST'])
def send():
	global Score_alphabet
	global BScore_alphabet
	if request.method == 'POST':
		try:
			url=request.form['imageconverted']
			guessing_number.download_image_ipg(url, 'predicting_number_file/images/', 'data')
			predicted_num=guessing_number.predict_num('predicting_number_file/images/data.png')
			num_to_detect = request.form['word_to_detect']
			a=str(predicted_num).strip()
			b=str(num_to_detect).strip()
			if(a==b):
				Score_alphabet = Score_alphabet +1
				if(Score_alphabet>BScore_alphabet):
					BScore_alphabet=Score_alphabet
			else:
				Score_alphabet=0

			return render_template('number.html',output="NUM: "+str(num_to_detect)+"\n"+"YOU: "+str(predicted_num), score="SCORE: "+str(Score_alphabet), best_score="BEST: "+str(BScore_alphabet))
		except:
			return render_template('number.html', output="PREDICTED NUMBER: ")
	return render_template('number.html')



if __name__ == '__main__':
    app.run(debug=True)
