import { s as F, j as x } from "./sveltify-j7R4x48E.js";
import { i as G, a as P, r as U, d as D, g as I, m as V } from "./Index--J1kEDq_.js";
const C = window.ms_globals.React, T = window.ms_globals.React.useMemo, k = window.ms_globals.React.useState, M = window.ms_globals.React.useEffect, B = window.ms_globals.React.forwardRef, H = window.ms_globals.React.useRef, $ = window.ms_globals.internalContext.useContextPropsContext, W = window.ms_globals.internalContext.ContextPropsProvider, z = window.ms_globals.ReactDOM.createPortal;
var X = /\s/;
function q(e) {
  for (var t = e.length; t-- && X.test(e.charAt(t)); )
    ;
  return t;
}
var J = /^\s+/;
function Q(e) {
  return e && e.slice(0, q(e) + 1).replace(J, "");
}
var L = NaN, Y = /^[-+]0x[0-9a-f]+$/i, Z = /^0b[01]+$/i, K = /^0o[0-7]+$/i, ee = parseInt;
function N(e) {
  if (typeof e == "number")
    return e;
  if (G(e))
    return L;
  if (P(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = P(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = Q(e);
  var r = Z.test(e);
  return r || K.test(e) ? ee(e.slice(2), r ? 2 : 8) : Y.test(e) ? L : +e;
}
var O = function() {
  return U.Date.now();
}, te = "Expected a function", ne = Math.max, re = Math.min;
function oe(e, t, r) {
  var s, a, n, o, i, d, h = 0, b = !1, l = !1, E = !0;
  if (typeof e != "function")
    throw new TypeError(te);
  t = N(t) || 0, P(r) && (b = !!r.leading, l = "maxWait" in r, n = l ? ne(N(r.maxWait) || 0, t) : n, E = "trailing" in r ? !!r.trailing : E);
  function f(c) {
    var g = s, w = a;
    return s = a = void 0, h = c, o = e.apply(w, g), o;
  }
  function S(c) {
    return h = c, i = setTimeout(m, t), b ? f(c) : o;
  }
  function u(c) {
    var g = c - d, w = c - h, A = t - g;
    return l ? re(A, n - w) : A;
  }
  function p(c) {
    var g = c - d, w = c - h;
    return d === void 0 || g >= t || g < 0 || l && w >= n;
  }
  function m() {
    var c = O();
    if (p(c))
      return _(c);
    i = setTimeout(m, u(c));
  }
  function _(c) {
    return i = void 0, E && s ? f(c) : (s = a = void 0, o);
  }
  function v() {
    i !== void 0 && clearTimeout(i), h = 0, s = d = a = i = void 0;
  }
  function R() {
    return i === void 0 ? o : _(O());
  }
  function y() {
    var c = O(), g = p(c);
    if (s = arguments, a = this, d = c, g) {
      if (i === void 0)
        return S(d);
      if (l)
        return clearTimeout(i), i = setTimeout(m, t), f(d);
    }
    return i === void 0 && (i = setTimeout(m, t)), o;
  }
  return y.cancel = v, y.flush = R, y;
}
function ie(e) {
  const [t, r] = k(() => I(e));
  return M(() => {
    let s = !0;
    return e.subscribe((n) => {
      s && (s = !1, n === t) || r(n);
    });
  }, [e]), t;
}
function se(e) {
  const t = T(() => D(e, (r) => r), [e]);
  return ie(t);
}
const ae = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function le(e) {
  return e ? Object.keys(e).reduce((t, r) => {
    const s = e[r];
    return t[r] = ce(r, s), t;
  }, {}) : {};
}
function ce(e, t) {
  return typeof t == "number" && !ae.includes(e) ? t + "px" : t;
}
function j(e) {
  const t = [], r = e.cloneNode(!1);
  if (e._reactElement) {
    const a = C.Children.toArray(e._reactElement.props.children).map((n) => {
      if (C.isValidElement(n) && n.props.__slot__) {
        const {
          portals: o,
          clonedElement: i
        } = j(n.props.el);
        return C.cloneElement(n, {
          ...n.props,
          el: i,
          children: [...C.Children.toArray(n.props.children), ...o]
        });
      }
      return null;
    });
    return a.originalChildren = e._reactElement.props.children, t.push(z(C.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: a
    }), r)), {
      clonedElement: r,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((a) => {
    e.getEventListeners(a).forEach(({
      listener: o,
      type: i,
      useCapture: d
    }) => {
      r.addEventListener(i, o, d);
    });
  });
  const s = Array.from(e.childNodes);
  for (let a = 0; a < s.length; a++) {
    const n = s[a];
    if (n.nodeType === 1) {
      const {
        clonedElement: o,
        portals: i
      } = j(n);
      t.push(...i), r.appendChild(o);
    } else n.nodeType === 3 && r.appendChild(n.cloneNode());
  }
  return {
    clonedElement: r,
    portals: t
  };
}
function de(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const ue = B(({
  slot: e,
  clone: t,
  className: r,
  style: s,
  observeAttributes: a
}, n) => {
  const o = H(), [i, d] = k([]), {
    forceClone: h
  } = $(), b = h ? !0 : t;
  return M(() => {
    var S;
    if (!o.current || !e)
      return;
    let l = e;
    function E() {
      let u = l;
      if (l.tagName.toLowerCase() === "svelte-slot" && l.children.length === 1 && l.children[0] && (u = l.children[0], u.tagName.toLowerCase() === "react-portal-target" && u.children[0] && (u = u.children[0])), de(n, u), r && u.classList.add(...r.split(" ")), s) {
        const p = le(s);
        Object.keys(p).forEach((m) => {
          u.style[m] = p[m];
        });
      }
    }
    let f = null;
    if (b && window.MutationObserver) {
      let u = function() {
        var v, R, y;
        (v = o.current) != null && v.contains(l) && ((R = o.current) == null || R.removeChild(l));
        const {
          portals: m,
          clonedElement: _
        } = j(e);
        l = _, d(m), l.style.display = "contents", E(), (y = o.current) == null || y.appendChild(l);
      };
      u();
      const p = oe(() => {
        u(), f == null || f.disconnect(), f == null || f.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: a
        });
      }, 50);
      f = new window.MutationObserver(p), f.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      l.style.display = "contents", E(), (S = o.current) == null || S.appendChild(l);
    return () => {
      var u, p;
      l.style.display = "", (u = o.current) != null && u.contains(l) && ((p = o.current) == null || p.removeChild(l)), f == null || f.disconnect();
    };
  }, [e, b, r, s, n, a]), C.createElement("react-child", {
    ref: o,
    style: {
      display: "contents"
    }
  }, ...i);
});
function fe(e, t) {
  const r = T(() => C.Children.toArray(e.originalChildren || e).filter((n) => n.props.node && !n.props.node.ignore && (!t && !n.props.nodeSlotKey || t && t === n.props.nodeSlotKey)).sort((n, o) => {
    if (n.props.node.slotIndex && o.props.node.slotIndex) {
      const i = I(n.props.node.slotIndex) || 0, d = I(o.props.node.slotIndex) || 0;
      return i - d === 0 && n.props.node.subSlotIndex && o.props.node.subSlotIndex ? (I(n.props.node.subSlotIndex) || 0) - (I(o.props.node.subSlotIndex) || 0) : i - d;
    }
    return 0;
  }).map((n) => n.props.node.target), [e, t]);
  return se(r);
}
const pe = ({
  value: e,
  children: t,
  contextValue: r
}) => {
  const s = T(() => typeof e != "object" || Array.isArray(e) ? {
    value: e
  } : e, [e]), a = T(() => V({}, r, s), [r, s]);
  return /* @__PURE__ */ x.jsx(W, {
    forceClone: !0,
    ctx: a,
    children: t
  });
}, he = F(({
  value: e,
  contextValue: t,
  children: r,
  __internal_slot_key: s
}) => {
  const a = fe(r, s);
  return /* @__PURE__ */ x.jsxs(x.Fragment, {
    children: [/* @__PURE__ */ x.jsx("div", {
      style: {
        display: "none"
      },
      children: /* @__PURE__ */ x.jsx(W, {
        children: r
      })
    }), e == null ? void 0 : e.map((n, o) => /* @__PURE__ */ x.jsx(pe, {
      value: n,
      contextValue: t,
      children: a.map((i, d) => /* @__PURE__ */ x.jsx(ue, {
        clone: !0,
        slot: i
      }, d))
    }, o))]
  });
});
export {
  he as Each,
  he as default
};
