css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.7rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #d5bdaf
}
.chat-message.bot {
    background-color: #ffdab9
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar{
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #03045e;
  font-size: 1.5rem;
  font-style: bold;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <h2 style="color: #9d0208;">Bot</h3>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <h2 style="color: #540b0e;">User</h3>   
    <div class="message">{{MSG}}</div>
</div>
'''


info_template = '''
    <div>
        <h3>{{INFO}}</h3>
    </div>
'''
