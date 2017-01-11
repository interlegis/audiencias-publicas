function chatAP() { // eslint-disable-line no-unused-vars
  const elements = {
    chat: $('.chat'),
    messages: $('.chat__messages'),
    messagesList: $('.messages__list'),
    readMore: $('.chat__read-more'),
    form: $('#chatform'),
    formInput: $('#message'),
  };

  const vars = {
    messagesHeight: () => elements.messages[0].offsetHeight,
    messagesScrollHeight: () => elements.messages[0].scrollHeight,
    messagesScrollTop: () => elements.messages[0].scrollTop,
    messagesListHeight: () => elements.messagesList[0].offsetHeight,
  };

  function isScrolledToBottom() {
    return vars.messagesScrollTop() === (vars.messagesScrollHeight() - vars.messagesHeight());
  }

  function scrollToBottom() {
    elements.messages[0].scrollTop = vars.messagesListHeight();
  }

  function animateToBottom() {
    elements.messages.animate({ scrollTop: vars.messagesListHeight() }, 'slow');
  }

  function showReadMore() {
    elements.readMore.removeClass('chat__read-more');
    elements.readMore.addClass('chat__read-more--visible');
  }

  function hideReadMore() {
    elements.readMore.removeClass('chat__read-more--visible');
    elements.readMore.addClass('chat__read-more');
  }

  function createClosedFormEl() {
    const closedFormEl = document.createElement('div');
    const closedFormSpanEl = document.createElement('span');

    closedFormEl.className = 'send-form--closed';
    closedFormSpanEl.innerHTML = 'Audiência encerrada para participações.';

    closedFormEl.appendChild(closedFormSpanEl);
    elements.chat[0].appendChild(closedFormEl);
  }

  function closeForm() {
    createClosedFormEl();
    elements.form.remove();
  }

  const events = {
    readMoreClick() {
      animateToBottom();
    },

    readMoreScroll() {
      if (isScrolledToBottom()) hideReadMore();
    },

    formInputKeyDown(event) {
      if (event.which === 13) event.preventDefault();
    },

    formInputKeyUp(event) {
      if (event.which === 13) elements.form.trigger('submit');
    },
  };

  (function bindEventsHandlers() {
    elements.messages.on('scroll', events.readMoreScroll);
    elements.readMore.on('click', events.readMoreClick);
    elements.formInput.on('keydown', events.formInputKeyDown);
    elements.formInput.on('keyup', events.formInputKeyUp);
  }());

  return {
    elements,
    isScrolledToBottom,
    scrollToBottom,
    showReadMore,
    closeForm,
  };
}
