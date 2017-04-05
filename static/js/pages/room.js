import createSocketHelper from '../helpers/create-socket';
import questionsComponent from '../components/questions';
import chatComponent from '../components/chat';
import tabsNavComponent from '../components/tabs-nav';
import characterCounterComponent from '../components/character-counter';
import onlineUsersComponent from '../components/online-users';

if (!closedRoom) {
  const onlineUsers = onlineUsersComponent();

  const questionsSocket = createSocketHelper('questions', 'questions/stream/');
  const chatSocket = createSocketHelper('chat', 'chat/stream/');

  chatSocket.socket.onopen = () => {
    console.log('Connected to chat socket'); // eslint-disable-line no-console
    onlineUsers.get();
  };

  questionsComponent(questionsSocket.socket);
  chatComponent(chatSocket.socket);

  window.onbeforeunload = () => {
    questionsSocket.close();
    chatSocket.close();
  };
}

tabsNavComponent();
characterCounterComponent();
