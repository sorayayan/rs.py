# -*- coding:UTF8 _*
#soraya chat bot telegram

import requests
import datetime

class BotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)
		#url = "https://api.telegram.org/bot<token>/")
    def get_updates(self, offset = 0, timeout = 100): 
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json
    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp
    def get_first_update(self):
        get_result = self.get_updates()
        if len(get_result) > 0:
            last_update = get_result[0]
        else:
            last_update = None
        return last_update

token = '747390761:AAFC-LbBzgVQh3fKU8ad5Z-XUq-8G0_0cbQ' #Token of your bot
magnito_bot = BotHandler(token) #Your bot's name


def main():
    new_offset = 0
    print('hi, now launching...')
    while True:
        all_updates = magnito_bot.get_updates(new_offset)
        if len(all_updates) > 0:
            for current_update in all_updates:
                print (current_update)
                first_update_id = current_update['update_id']
                if 'text' not in current_update ['message']:
                    first_chat_text='New member'
                else:
                    first_chat_text = current_update['message']['text']
                    first_chat_id = current_update['message']['chat']['id']
                if 'first_name' in current_update['message']:
                    first_chat_name = current_update['message']['chat']['first_name']
                elif 'new_chat_member' in current_update['message']:
                    first_chat_name = current_update['message']['new_chat_member']['username']
                elif 'from' in current_update['message']:
                    first_chat_name = current_update['message']['from']['first_name']
                else:
                    first_chat_name = "unknown"

                if first_chat_text == '/start' or  first_chat_text == 'Star' or  first_chat_text == 'Start' or  first_chat_text == 'star':
                   magnito_bot.send_message(first_chat_id, 'Selamat datang ' + first_chat_name + '.\n\n-->Menyapa, Silahkan ketik:\n"hy, hai, hi, hu, pagi, siang, malam"\n\n-->Informasi, Silahkan ketik:\n"PENDAFTARAN, JAMINAN KESEHATAN, JADWAL DOKTER"\n\n-->Form survey, Silahkan ketik:\n"SURVEY"\n\n-->Kalkulator, Silahkan input:\nAngka dan operator\n\n-->Kalkulasi Umur, Silahkan input:\nTahun lahir anda\n\n-->Lupa perintah dalam bot, Ketik:\n"help"')
                   new_offset = first_update_id+ 1
                elif first_chat_text == 'hy' or first_chat_text == 'Hy' or first_chat_text == 'HY' or first_chat_text == 'hai' or first_chat_text == 'Hai' or first_chat_text == 'HAI' or first_chat_text == 'hi' or first_chat_text == 'Hi' or first_chat_text == 'HI' or first_chat_text == 'hu' or first_chat_text == 'Hu' or first_chat_text == 'HU':
                     magnito_bot.send_message(first_chat_id, 'Hallo ' + first_chat_name)
                     new_offset = first_update_id+ 1 
                elif first_chat_text == 'HELP' or first_chat_text == 'Help' or first_chat_text == 'help':
					magnito_bot.send_message(first_chat_id, 'Layanan yang disediakan oleh Bot, yaitu:' + '\n\n-->Menyapa, Silahkan ketik:\n"hy, hai, hi, hu, pagi, siang, malam"\n\n-->Informasi, Silahkan ketik:\n"PENDAFTARAN, JAMINAN KESEHATAN, JADWAL DOKTER"\n\n-->Form survey, Silahkan ketik:\n"SURVEY"\n\n-->Kalkulator, Silahkan input:\nAngka dan operator\n\n-->Kalkulasi Umur, Silahkan input:\nTahun lahir anda\n\n-->Lupa perintah dalam bot, Ketik:\n"help"')
					new_offset = first_update_id+ 1
                elif first_chat_text == 'Pagi' or first_chat_text == 'pagi' or first_chat_text == 'PAGI' or first_chat_text == 'Siang' or first_chat_text == 'siang' or first_chat_text == 'SIANG' or first_chat_text == 'Malam' or first_chat_text == 'malam' or first_chat_text == 'MALAM':
                    magnito_bot.send_message(first_chat_id, first_chat_text+ ' juga ' + first_chat_name)
                    new_offset = first_update_id+ 1
                elif first_chat_text == 'PENDAFTARAN' or first_chat_text == 'Pendaftaran' or first_chat_text == 'pendaftaran' :
                    magnito_bot.send_message(first_chat_id, 'Pendaftaran terbagi menjadi dua, yaitu:\nP.1. Pendaftaran Langsung \nP.2. Pendaftaran Online (jika sebelumnya sudah pernah berobat/khusus) \n\n->> Ketik: "P.1/P.2"')
                    new_offset = first_update_id+ 1
                elif first_chat_text == 'P.1' or first_chat_text == 'p.1':
                    magnito_bot.send_message(first_chat_id, 'Pendaftaran langsung, silahkan mengunjungi RS.PUPUK KALTIM (Alamat : Jl. Oxigen No.01, Guntung, Bontang Utara, Kota Bontang, Kalimantan Timur 75313)')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'P.2' or first_chat_text == 'p.2':
                    magnito_bot.send_message(first_chat_id, 'Silahkan kunjungi https://arteri.rspkt.com/aorta/')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'JAMINAN KESEHATAN' or first_chat_text == 'Jaminan kesehatan' or first_chat_text == 'jaminan kesehatan':
                    magnito_bot.send_message(first_chat_id, 'Jaminan kesehatan terbagi menjadi tiga, yaitu: \nJ.1. Umum \nJ.2. BPJS Kesehatan (Mandiri) \nJ.3. BPJS Kesehatan(KIS) \n\n->> Ketik: J.1/J.2/J.3"')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'J.1' or first_chat_text == 'j.1':
                    magnito_bot.send_message(first_chat_id, 'Persyaratan Layanan Umum, yaitu: \n-Nomor Telpon \n-Nama Pasien \n-Alamat Pasien')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'J.2' or first_chat_text == 'j.2':
                    magnito_bot.send_message(first_chat_id, 'Persyaratan Layanan BPJS Kesehatan (Mandiri RS PKT Group), yaitu: \n-Menunjukkan Kartu BPJS Kesehatan (Mandiri) \n\nCara Daftar : \n1. Photo copy KK \n2. Photo copy KTP \n3. Photo copy NPWP (jika ada) \n4. Pas photo ukuran 3X4 (1 lembar), No.HP \n5. Nomor rekening (Bank Mandiri, BRI, BNI) \n6. Pilihan kelas perawatan \n\t\t\t\t\tkelas I: Rp.59.500,- \n\t\t\t\t\tkelas II: Rp.42.500,- \n\t\t\t\t\tkelas III: Rp.25.500,- \n\n->Layanan : Unit pendaftaran RS.PKT Bontang, marketing@rspkt.com \n\n->Informasi: 0548-41118 EXT.218 atau 0811 584 8000')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'J.3' or first_chat_text == 'j.3':
                    magnito_bot.send_message(first_chat_id, 'Persyaratan Layanan BPJS Kesehatan (KIS) yaitu: \n-Menunjukkan Kartu BPJS Kesehatan (KIS) \n-Surat Rujukan \n\nCara Daftar : \n1. Photo copy KK \n2. Photo copy KTP \n3. Surat keterangan tidak mampu dari RT/RW dan kelurahan setempat \n4. Surat pengantar dari puskesmas \n\n->Layanan : Dinas Kesehatan Kota Bontang (Alamat: Jl. Jenderal Ahmad Yani No.31, Api-Api, Bontang Utara, Kota Bontang, Kalimantan Timur 75311)')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'JADWAL DOKTER' or first_chat_text == 'Jadwal dokter' or first_chat_text == 'jadwal dokter':
                    magnito_bot.send_message(first_chat_id, 'Silahkan kunjungi : https://arteri.rspkt.com/aorta/jadwal/')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'SURVEY' or first_chat_text == 'Survey' or first_chat_text == 'survey':
                    magnito_bot.send_message(first_chat_id, 'Setiap pasien wajib mengisikan form survey RS.PUPUK KALTIM (PT. KALTIM MEDIKA UTAMA) \n\nSilahkan kunjungi : http://10.10.10.110:5000/')
                    new_offset = first_update_id + 1
                elif first_chat_text == '.' or first_chat_text == ',' or first_chat_text == '?' or first_chat_text == '!':
                    magnito_bot.send_message(first_chat_id, first_chat_name + ', tunggu ya saya lagi sibuk nih!')
                    new_offset = first_update_id+ 1
                elif first_chat_text == 'terimakasih' or first_chat_text == 'terimakasih informasinya':
                    magnito_bot.send_message(first_chat_id, 'Sama-Sama ' + first_chat_name + 'Semoga puas dengan pelayanan kami :)')
                    new_offset = first_update_id+ 1
                elif first_chat_text.isdigit():
					year = datetime.datetime.now().year
					year_of_birth = int(first_chat_text)
					magnito_bot.send_message (first_chat_id, (year-year_of_birth))
					new_offset = first_update_id+ 1
                else:
                        try:
                            variabelchat = eval(first_chat_text)
                            magnito_bot.send_message(first_chat_id, variabelchat)
                            new_offset = first_update_id + 1
                        except Exception as e:
                            magnito_bot.send_message(first_chat_id,'Maaf keyword "' + first_chat_text + '" tidak terdaftar')
                            new_offset = first_update_id+ 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit ()
