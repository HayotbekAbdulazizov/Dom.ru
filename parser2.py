


def schedule_api():
	r = requests.get("https://kun.uz/news/list")
	soup = BeautifulSoup(r.text, 'html.parser')
	cd_headings = soup.findAll("a", {"class": "daily-block l-item"})

	print(len(cd_headings))

    
	for th in soup.findAll("a", {"class": "daily-block l-item"}):
		href = th['href']
		slug = slugify(href)
		post_url = f"https://kun.uz{href}"
		single_r = requests.get(post_url)
		single_soup = BeautifulSoup(single_r.text, 'html.parser')
		view = single_soup.find("div", {"class": "view"}).text
		title = single_soup.find('div', {"class":"single-header__title"}).text	
		body_code = single_soup.find('div', {"class":"single-content"})

		main_img_ls = body_code.findAll('img')
		paragraphs = body_code.findAll('p')

		main_img = ''

		if len(main_img_ls) != 0:
			main_img = main_img_ls[0]['src']
		else:
			main_img = 'https://storage.kun.uz/source/thumbnails/_medium/7/L88XGffdJ2B1z7VmOZQTVboR-FMgL2mP_medium.jpg'

		body = str(body_code)


		try :
			post = Post.objects.get(slug=str(slug))
			post.source = post_url
			post.image = main_img
			post.save()
		except :
			Post.objects.create( rich_body=str(body_code) ,slug=slug, title=title, views=view, likes=0, source=post_url, image=main_img)
			CreatePage(title, html_content=body_code)
			tg_link = CreatePage(title, body_code)
			bot.send_photo(
			parse_mode='HTML',
			chat_id=channel_id, 
			photo=main_img, 
			caption=f' <b> {title} </b>  \n   {str(paragraphs[0].text) } \n \n  {tg_link} \n \n \n 	')
			bot.send_message(parse_mode='HTML', text=f" <b> {title} </b> \n \n {paragraphs[0].text} ", chat_id=channel_id)

		# print(title, 'Title')
		# print(slug, 'Slug')
		# print(post_url, ' Post Url')
		# print(view, 'views')
		# print(body[:20], 'Body Code')
		# print(main_img, 'Main IMG')

		# Translation UZ_RU
		print('TITLE_RU', translate(to_latin(title),src='uz', to='ru'))
		print('TITLE_RU', translate(to_latin(title),src='uz', to='ru'))
		print('TITLE_RU', translate(to_latin(title),src='uz', to='ru'))

		print
		print('all')
		print('=================================================================')
		time.sleep(1)
	return True

	# https://localazy.com/my/community