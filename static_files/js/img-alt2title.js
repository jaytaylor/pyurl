
function browserdetect() {
  var agent = navigator.userAgent.toLowerCase();
  this.isIE      = agent.indexOf("msie") > -1;
  this.ieVer = this.isIE ? /msie\s(\d\.\d)/.exec(agent)[1] : 0;
  this.isMoz     = agent.indexOf('firefox') != -1;
  this.isSafari  = agent.indexOf('safari') != -1;
  this.quirksMode= this.isIE && (!document.compatMode || document.compatMode.indexOf("BackCompat") > -1);
  this.isOp      = 'opera' in window;
  this.isWebKit  = agent.indexOf('webkit') != -1;
  if (this.isIE) {
    this.get_style = function(obj, prop) {
      if (!(prop in obj.currentStyle)) return "";
      var matches = /^([\d.]+)(\w*)/.exec(obj.currentStyle[prop]);
      if (!matches) return obj.currentStyle[prop];
      if (matches[1] == 0) return '0';
      // now convert to pixels if necessary
      if (matches[2] && matches[2] !== 'px') {
        var style = obj.style.left;
        var rtStyle = obj.runtimeStyle.left;
        obj.runtimeStyle.left = obj.currentStyle.left;
        obj.style.left = matches[1] + matches[2];
        matches[0] = obj.style.pixelLeft;
        obj.style.left = style;
        obj.runtimeStyle.left = rtStyle;
      }
      return matches[0];
    };
  }
  else {
    this.get_style = function(obj, prop) {
      prop = prop.replace(/([a-z])([A-Z])/g, '$1-$2').toLowerCase();
      return document.defaultView.getComputedStyle(obj, '').getPropertyValue(prop);
    };
  }
}

// Cross browser add event wrapper

function addEvent(elm, evType, fn, useCapture) {
  if (elm.addEventListener) {
    elm.addEventListener(evType, fn, useCapture);
    return true;
  }
  if (elm.attachEvent) return elm.attachEvent('on' + evType, fn);
  elm['on' + evType] = fn;
  return false;
}

function alt2title() {
  var imgs = document.getElementsByTagName('img');
  for (var i = 0; i < imgs.length; ++i)
    if(imgs[i].title=='')
      imgs[i].title=imgs[i].alt;
}

var alt2titleBrowser = new browserdetect;
  
if (alt2titleBrowser.isOp)
  document.addEventListener("DOMContentLoaded", alt2title, false);
else
  addEvent(window, 'load', alt2title, false);
