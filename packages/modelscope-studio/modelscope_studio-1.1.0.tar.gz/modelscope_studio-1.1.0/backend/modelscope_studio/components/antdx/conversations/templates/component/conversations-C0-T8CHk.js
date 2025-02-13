import { i as Zt, a as Ie, r as Yt, g as er, w as Z, c as te, b as xt } from "./Index-C2AlqOSG.js";
const F = window.ms_globals.React, b = window.ms_globals.React, Kt = window.ms_globals.React.forwardRef, qt = window.ms_globals.React.useRef, Qt = window.ms_globals.React.useState, Jt = window.ms_globals.React.useEffect, Me = window.ms_globals.React.useMemo, Pe = window.ms_globals.ReactDOM.createPortal, tr = window.ms_globals.internalContext.useContextPropsContext, re = window.ms_globals.internalContext.ContextPropsProvider, St = window.ms_globals.createItemsContext.createItemsContext, rr = window.ms_globals.antd.ConfigProvider, je = window.ms_globals.antd.theme, Ct = window.ms_globals.antd.Typography, nr = window.ms_globals.antd.Tooltip, or = window.ms_globals.antd.Dropdown, ir = window.ms_globals.antdIcons.EllipsisOutlined, ne = window.ms_globals.antdCssinjs.unit, xe = window.ms_globals.antdCssinjs.token2CSSVar, Ue = window.ms_globals.antdCssinjs.useStyleRegister, sr = window.ms_globals.antdCssinjs.useCSSVarRegister, ar = window.ms_globals.antdCssinjs.createTheme, lr = window.ms_globals.antdCssinjs.useCacheToken;
var cr = /\s/;
function ur(t) {
  for (var e = t.length; e-- && cr.test(t.charAt(e)); )
    ;
  return e;
}
var fr = /^\s+/;
function dr(t) {
  return t && t.slice(0, ur(t) + 1).replace(fr, "");
}
var We = NaN, hr = /^[-+]0x[0-9a-f]+$/i, gr = /^0b[01]+$/i, pr = /^0o[0-7]+$/i, mr = parseInt;
function Ke(t) {
  if (typeof t == "number")
    return t;
  if (Zt(t))
    return We;
  if (Ie(t)) {
    var e = typeof t.valueOf == "function" ? t.valueOf() : t;
    t = Ie(e) ? e + "" : e;
  }
  if (typeof t != "string")
    return t === 0 ? t : +t;
  t = dr(t);
  var n = gr.test(t);
  return n || pr.test(t) ? mr(t.slice(2), n ? 2 : 8) : hr.test(t) ? We : +t;
}
var Se = function() {
  return Yt.Date.now();
}, br = "Expected a function", yr = Math.max, vr = Math.min;
function xr(t, e, n) {
  var o, r, i, s, a, l, c = 0, f = !1, u = !1, d = !0;
  if (typeof t != "function")
    throw new TypeError(br);
  e = Ke(e) || 0, Ie(n) && (f = !!n.leading, u = "maxWait" in n, i = u ? yr(Ke(n.maxWait) || 0, e) : i, d = "trailing" in n ? !!n.trailing : d);
  function g(x) {
    var O = o, M = r;
    return o = r = void 0, c = x, s = t.apply(M, O), s;
  }
  function y(x) {
    return c = x, a = setTimeout(v, e), f ? g(x) : s;
  }
  function h(x) {
    var O = x - l, M = x - c, P = e - O;
    return u ? vr(P, i - M) : P;
  }
  function m(x) {
    var O = x - l, M = x - c;
    return l === void 0 || O >= e || O < 0 || u && M >= i;
  }
  function v() {
    var x = Se();
    if (m(x))
      return S(x);
    a = setTimeout(v, h(x));
  }
  function S(x) {
    return a = void 0, d && o ? g(x) : (o = r = void 0, s);
  }
  function E() {
    a !== void 0 && clearTimeout(a), c = 0, o = l = r = a = void 0;
  }
  function p() {
    return a === void 0 ? s : S(Se());
  }
  function C() {
    var x = Se(), O = m(x);
    if (o = arguments, r = this, l = x, O) {
      if (a === void 0)
        return y(l);
      if (u)
        return clearTimeout(a), a = setTimeout(v, e), g(l);
    }
    return a === void 0 && (a = setTimeout(v, e)), s;
  }
  return C.cancel = E, C.flush = p, C;
}
var _t = {
  exports: {}
}, ae = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Sr = b, Cr = Symbol.for("react.element"), _r = Symbol.for("react.fragment"), wr = Object.prototype.hasOwnProperty, Or = Sr.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Tr = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function wt(t, e, n) {
  var o, r = {}, i = null, s = null;
  n !== void 0 && (i = "" + n), e.key !== void 0 && (i = "" + e.key), e.ref !== void 0 && (s = e.ref);
  for (o in e) wr.call(e, o) && !Tr.hasOwnProperty(o) && (r[o] = e[o]);
  if (t && t.defaultProps) for (o in e = t.defaultProps, e) r[o] === void 0 && (r[o] = e[o]);
  return {
    $$typeof: Cr,
    type: t,
    key: i,
    ref: s,
    props: r,
    _owner: Or.current
  };
}
ae.Fragment = _r;
ae.jsx = wt;
ae.jsxs = wt;
_t.exports = ae;
var D = _t.exports;
const {
  SvelteComponent: Er,
  assign: qe,
  binding_callbacks: Qe,
  check_outros: Mr,
  children: Ot,
  claim_element: Tt,
  claim_space: Pr,
  component_subscribe: Je,
  compute_slots: Ir,
  create_slot: jr,
  detach: U,
  element: Et,
  empty: Ze,
  exclude_internal_props: Ye,
  get_all_dirty_from_scope: kr,
  get_slot_changes: Lr,
  group_outros: Rr,
  init: Dr,
  insert_hydration: Y,
  safe_not_equal: Hr,
  set_custom_element_data: Mt,
  space: Ar,
  transition_in: ee,
  transition_out: ke,
  update_slot_base: $r
} = window.__gradio__svelte__internal, {
  beforeUpdate: zr,
  getContext: Br,
  onDestroy: Xr,
  setContext: Fr
} = window.__gradio__svelte__internal;
function et(t) {
  let e, n;
  const o = (
    /*#slots*/
    t[7].default
  ), r = jr(
    o,
    t,
    /*$$scope*/
    t[6],
    null
  );
  return {
    c() {
      e = Et("svelte-slot"), r && r.c(), this.h();
    },
    l(i) {
      e = Tt(i, "SVELTE-SLOT", {
        class: !0
      });
      var s = Ot(e);
      r && r.l(s), s.forEach(U), this.h();
    },
    h() {
      Mt(e, "class", "svelte-1rt0kpf");
    },
    m(i, s) {
      Y(i, e, s), r && r.m(e, null), t[9](e), n = !0;
    },
    p(i, s) {
      r && r.p && (!n || s & /*$$scope*/
      64) && $r(
        r,
        o,
        i,
        /*$$scope*/
        i[6],
        n ? Lr(
          o,
          /*$$scope*/
          i[6],
          s,
          null
        ) : kr(
          /*$$scope*/
          i[6]
        ),
        null
      );
    },
    i(i) {
      n || (ee(r, i), n = !0);
    },
    o(i) {
      ke(r, i), n = !1;
    },
    d(i) {
      i && U(e), r && r.d(i), t[9](null);
    }
  };
}
function Vr(t) {
  let e, n, o, r, i = (
    /*$$slots*/
    t[4].default && et(t)
  );
  return {
    c() {
      e = Et("react-portal-target"), n = Ar(), i && i.c(), o = Ze(), this.h();
    },
    l(s) {
      e = Tt(s, "REACT-PORTAL-TARGET", {
        class: !0
      }), Ot(e).forEach(U), n = Pr(s), i && i.l(s), o = Ze(), this.h();
    },
    h() {
      Mt(e, "class", "svelte-1rt0kpf");
    },
    m(s, a) {
      Y(s, e, a), t[8](e), Y(s, n, a), i && i.m(s, a), Y(s, o, a), r = !0;
    },
    p(s, [a]) {
      /*$$slots*/
      s[4].default ? i ? (i.p(s, a), a & /*$$slots*/
      16 && ee(i, 1)) : (i = et(s), i.c(), ee(i, 1), i.m(o.parentNode, o)) : i && (Rr(), ke(i, 1, 1, () => {
        i = null;
      }), Mr());
    },
    i(s) {
      r || (ee(i), r = !0);
    },
    o(s) {
      ke(i), r = !1;
    },
    d(s) {
      s && (U(e), U(n), U(o)), t[8](null), i && i.d(s);
    }
  };
}
function tt(t) {
  const {
    svelteInit: e,
    ...n
  } = t;
  return n;
}
function Nr(t, e, n) {
  let o, r, {
    $$slots: i = {},
    $$scope: s
  } = e;
  const a = Ir(i);
  let {
    svelteInit: l
  } = e;
  const c = Z(tt(e)), f = Z();
  Je(t, f, (p) => n(0, o = p));
  const u = Z();
  Je(t, u, (p) => n(1, r = p));
  const d = [], g = Br("$$ms-gr-react-wrapper"), {
    slotKey: y,
    slotIndex: h,
    subSlotIndex: m
  } = er() || {}, v = l({
    parent: g,
    props: c,
    target: f,
    slot: u,
    slotKey: y,
    slotIndex: h,
    subSlotIndex: m,
    onDestroy(p) {
      d.push(p);
    }
  });
  Fr("$$ms-gr-react-wrapper", v), zr(() => {
    c.set(tt(e));
  }), Xr(() => {
    d.forEach((p) => p());
  });
  function S(p) {
    Qe[p ? "unshift" : "push"](() => {
      o = p, f.set(o);
    });
  }
  function E(p) {
    Qe[p ? "unshift" : "push"](() => {
      r = p, u.set(r);
    });
  }
  return t.$$set = (p) => {
    n(17, e = qe(qe({}, e), Ye(p))), "svelteInit" in p && n(5, l = p.svelteInit), "$$scope" in p && n(6, s = p.$$scope);
  }, e = Ye(e), [o, r, f, u, a, l, s, i, S, E];
}
class Gr extends Er {
  constructor(e) {
    super(), Dr(this, e, Nr, Vr, Hr, {
      svelteInit: 5
    });
  }
}
const rt = window.ms_globals.rerender, Ce = window.ms_globals.tree;
function Ur(t, e = {}) {
  function n(o) {
    const r = Z(), i = new Gr({
      ...o,
      props: {
        svelteInit(s) {
          window.ms_globals.autokey += 1;
          const a = {
            key: window.ms_globals.autokey,
            svelteInstance: r,
            reactComponent: t,
            props: s.props,
            slot: s.slot,
            target: s.target,
            slotIndex: s.slotIndex,
            subSlotIndex: s.subSlotIndex,
            ignore: e.ignore,
            slotKey: s.slotKey,
            nodes: []
          }, l = s.parent ?? Ce;
          return l.nodes = [...l.nodes, a], rt({
            createPortal: Pe,
            node: Ce
          }), s.onDestroy(() => {
            l.nodes = l.nodes.filter((c) => c.svelteInstance !== r), rt({
              createPortal: Pe,
              node: Ce
            });
          }), a;
        },
        ...o.props
      }
    });
    return r.set(i), i;
  }
  return new Promise((o) => {
    window.ms_globals.initializePromise.then(() => {
      o(n);
    });
  });
}
const Wr = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function Kr(t) {
  return t ? Object.keys(t).reduce((e, n) => {
    const o = t[n];
    return e[n] = qr(n, o), e;
  }, {}) : {};
}
function qr(t, e) {
  return typeof e == "number" && !Wr.includes(t) ? e + "px" : e;
}
function Le(t) {
  const e = [], n = t.cloneNode(!1);
  if (t._reactElement) {
    const r = b.Children.toArray(t._reactElement.props.children).map((i) => {
      if (b.isValidElement(i) && i.props.__slot__) {
        const {
          portals: s,
          clonedElement: a
        } = Le(i.props.el);
        return b.cloneElement(i, {
          ...i.props,
          el: a,
          children: [...b.Children.toArray(i.props.children), ...s]
        });
      }
      return null;
    });
    return r.originalChildren = t._reactElement.props.children, e.push(Pe(b.cloneElement(t._reactElement, {
      ...t._reactElement.props,
      children: r
    }), n)), {
      clonedElement: n,
      portals: e
    };
  }
  Object.keys(t.getEventListeners()).forEach((r) => {
    t.getEventListeners(r).forEach(({
      listener: s,
      type: a,
      useCapture: l
    }) => {
      n.addEventListener(a, s, l);
    });
  });
  const o = Array.from(t.childNodes);
  for (let r = 0; r < o.length; r++) {
    const i = o[r];
    if (i.nodeType === 1) {
      const {
        clonedElement: s,
        portals: a
      } = Le(i);
      e.push(...a), n.appendChild(s);
    } else i.nodeType === 3 && n.appendChild(i.cloneNode());
  }
  return {
    clonedElement: n,
    portals: e
  };
}
function Qr(t, e) {
  t && (typeof t == "function" ? t(e) : t.current = e);
}
const oe = Kt(({
  slot: t,
  clone: e,
  className: n,
  style: o,
  observeAttributes: r
}, i) => {
  const s = qt(), [a, l] = Qt([]), {
    forceClone: c
  } = tr(), f = c ? !0 : e;
  return Jt(() => {
    var y;
    if (!s.current || !t)
      return;
    let u = t;
    function d() {
      let h = u;
      if (u.tagName.toLowerCase() === "svelte-slot" && u.children.length === 1 && u.children[0] && (h = u.children[0], h.tagName.toLowerCase() === "react-portal-target" && h.children[0] && (h = h.children[0])), Qr(i, h), n && h.classList.add(...n.split(" ")), o) {
        const m = Kr(o);
        Object.keys(m).forEach((v) => {
          h.style[v] = m[v];
        });
      }
    }
    let g = null;
    if (f && window.MutationObserver) {
      let h = function() {
        var E, p, C;
        (E = s.current) != null && E.contains(u) && ((p = s.current) == null || p.removeChild(u));
        const {
          portals: v,
          clonedElement: S
        } = Le(t);
        u = S, l(v), u.style.display = "contents", d(), (C = s.current) == null || C.appendChild(u);
      };
      h();
      const m = xr(() => {
        h(), g == null || g.disconnect(), g == null || g.observe(t, {
          childList: !0,
          subtree: !0,
          attributes: r
        });
      }, 50);
      g = new window.MutationObserver(m), g.observe(t, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      u.style.display = "contents", d(), (y = s.current) == null || y.appendChild(u);
    return () => {
      var h, m;
      u.style.display = "", (h = s.current) != null && h.contains(u) && ((m = s.current) == null || m.removeChild(u)), g == null || g.disconnect();
    };
  }, [t, f, n, o, i, r]), b.createElement("react-child", {
    ref: s,
    style: {
      display: "contents"
    }
  }, ...a);
}), Jr = "1.0.5", Zr = /* @__PURE__ */ b.createContext({}), Yr = {
  classNames: {},
  styles: {},
  className: "",
  style: {}
}, en = (t) => {
  const e = b.useContext(Zr);
  return b.useMemo(() => ({
    ...Yr,
    ...e[t]
  }), [e[t]]);
};
function ie() {
  return ie = Object.assign ? Object.assign.bind() : function(t) {
    for (var e = 1; e < arguments.length; e++) {
      var n = arguments[e];
      for (var o in n) ({}).hasOwnProperty.call(n, o) && (t[o] = n[o]);
    }
    return t;
  }, ie.apply(null, arguments);
}
function Re() {
  const {
    getPrefixCls: t,
    direction: e,
    csp: n,
    iconPrefixCls: o,
    theme: r
  } = b.useContext(rr.ConfigContext);
  return {
    theme: r,
    getPrefixCls: t,
    direction: e,
    csp: n,
    iconPrefixCls: o
  };
}
function nt(t) {
  var e = F.useRef();
  e.current = t;
  var n = F.useCallback(function() {
    for (var o, r = arguments.length, i = new Array(r), s = 0; s < r; s++)
      i[s] = arguments[s];
    return (o = e.current) === null || o === void 0 ? void 0 : o.call.apply(o, [e].concat(i));
  }, []);
  return n;
}
function tn(t) {
  if (Array.isArray(t)) return t;
}
function rn(t, e) {
  var n = t == null ? null : typeof Symbol < "u" && t[Symbol.iterator] || t["@@iterator"];
  if (n != null) {
    var o, r, i, s, a = [], l = !0, c = !1;
    try {
      if (i = (n = n.call(t)).next, e === 0) {
        if (Object(n) !== n) return;
        l = !1;
      } else for (; !(l = (o = i.call(n)).done) && (a.push(o.value), a.length !== e); l = !0) ;
    } catch (f) {
      c = !0, r = f;
    } finally {
      try {
        if (!l && n.return != null && (s = n.return(), Object(s) !== s)) return;
      } finally {
        if (c) throw r;
      }
    }
    return a;
  }
}
function ot(t, e) {
  (e == null || e > t.length) && (e = t.length);
  for (var n = 0, o = Array(e); n < e; n++) o[n] = t[n];
  return o;
}
function nn(t, e) {
  if (t) {
    if (typeof t == "string") return ot(t, e);
    var n = {}.toString.call(t).slice(8, -1);
    return n === "Object" && t.constructor && (n = t.constructor.name), n === "Map" || n === "Set" ? Array.from(t) : n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n) ? ot(t, e) : void 0;
  }
}
function on() {
  throw new TypeError(`Invalid attempt to destructure non-iterable instance.
In order to be iterable, non-array objects must have a [Symbol.iterator]() method.`);
}
function N(t, e) {
  return tn(t) || rn(t, e) || nn(t, e) || on();
}
function sn() {
  return !!(typeof window < "u" && window.document && window.document.createElement);
}
var it = sn() ? F.useLayoutEffect : F.useEffect, an = function(e, n) {
  var o = F.useRef(!0);
  it(function() {
    return e(o.current);
  }, n), it(function() {
    return o.current = !1, function() {
      o.current = !0;
    };
  }, []);
}, st = function(e, n) {
  an(function(o) {
    if (!o)
      return e();
  }, n);
};
function at(t) {
  var e = F.useRef(!1), n = F.useState(t), o = N(n, 2), r = o[0], i = o[1];
  F.useEffect(function() {
    return e.current = !1, function() {
      e.current = !0;
    };
  }, []);
  function s(a, l) {
    l && e.current || i(a);
  }
  return [r, s];
}
function _e(t) {
  return t !== void 0;
}
function ln(t, e) {
  var n = e || {}, o = n.defaultValue, r = n.value, i = n.onChange, s = n.postState, a = at(function() {
    return _e(r) ? r : _e(o) ? typeof o == "function" ? o() : o : typeof t == "function" ? t() : t;
  }), l = N(a, 2), c = l[0], f = l[1], u = r !== void 0 ? r : c, d = s ? s(u) : u, g = nt(i), y = at([u]), h = N(y, 2), m = h[0], v = h[1];
  st(function() {
    var E = m[0];
    c !== E && g(c, E);
  }, [m]), st(function() {
    _e(r) || f(r);
  }, [r]);
  var S = nt(function(E, p) {
    f(E, p), v([u], p);
  });
  return [d, S];
}
function A(t) {
  "@babel/helpers - typeof";
  return A = typeof Symbol == "function" && typeof Symbol.iterator == "symbol" ? function(e) {
    return typeof e;
  } : function(e) {
    return e && typeof Symbol == "function" && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e;
  }, A(t);
}
var w = {};
/**
 * @license React
 * react-is.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var $e = Symbol.for("react.element"), ze = Symbol.for("react.portal"), le = Symbol.for("react.fragment"), ce = Symbol.for("react.strict_mode"), ue = Symbol.for("react.profiler"), fe = Symbol.for("react.provider"), de = Symbol.for("react.context"), cn = Symbol.for("react.server_context"), he = Symbol.for("react.forward_ref"), ge = Symbol.for("react.suspense"), pe = Symbol.for("react.suspense_list"), me = Symbol.for("react.memo"), be = Symbol.for("react.lazy"), un = Symbol.for("react.offscreen"), Pt;
Pt = Symbol.for("react.module.reference");
function H(t) {
  if (typeof t == "object" && t !== null) {
    var e = t.$$typeof;
    switch (e) {
      case $e:
        switch (t = t.type, t) {
          case le:
          case ue:
          case ce:
          case ge:
          case pe:
            return t;
          default:
            switch (t = t && t.$$typeof, t) {
              case cn:
              case de:
              case he:
              case be:
              case me:
              case fe:
                return t;
              default:
                return e;
            }
        }
      case ze:
        return e;
    }
  }
}
w.ContextConsumer = de;
w.ContextProvider = fe;
w.Element = $e;
w.ForwardRef = he;
w.Fragment = le;
w.Lazy = be;
w.Memo = me;
w.Portal = ze;
w.Profiler = ue;
w.StrictMode = ce;
w.Suspense = ge;
w.SuspenseList = pe;
w.isAsyncMode = function() {
  return !1;
};
w.isConcurrentMode = function() {
  return !1;
};
w.isContextConsumer = function(t) {
  return H(t) === de;
};
w.isContextProvider = function(t) {
  return H(t) === fe;
};
w.isElement = function(t) {
  return typeof t == "object" && t !== null && t.$$typeof === $e;
};
w.isForwardRef = function(t) {
  return H(t) === he;
};
w.isFragment = function(t) {
  return H(t) === le;
};
w.isLazy = function(t) {
  return H(t) === be;
};
w.isMemo = function(t) {
  return H(t) === me;
};
w.isPortal = function(t) {
  return H(t) === ze;
};
w.isProfiler = function(t) {
  return H(t) === ue;
};
w.isStrictMode = function(t) {
  return H(t) === ce;
};
w.isSuspense = function(t) {
  return H(t) === ge;
};
w.isSuspenseList = function(t) {
  return H(t) === pe;
};
w.isValidElementType = function(t) {
  return typeof t == "string" || typeof t == "function" || t === le || t === ue || t === ce || t === ge || t === pe || t === un || typeof t == "object" && t !== null && (t.$$typeof === be || t.$$typeof === me || t.$$typeof === fe || t.$$typeof === de || t.$$typeof === he || t.$$typeof === Pt || t.getModuleId !== void 0);
};
w.typeOf = H;
function fn(t, e) {
  if (A(t) != "object" || !t) return t;
  var n = t[Symbol.toPrimitive];
  if (n !== void 0) {
    var o = n.call(t, e || "default");
    if (A(o) != "object") return o;
    throw new TypeError("@@toPrimitive must return a primitive value.");
  }
  return (e === "string" ? String : Number)(t);
}
function It(t) {
  var e = fn(t, "string");
  return A(e) == "symbol" ? e : e + "";
}
function T(t, e, n) {
  return (e = It(e)) in t ? Object.defineProperty(t, e, {
    value: n,
    enumerable: !0,
    configurable: !0,
    writable: !0
  }) : t[e] = n, t;
}
function lt(t, e) {
  var n = Object.keys(t);
  if (Object.getOwnPropertySymbols) {
    var o = Object.getOwnPropertySymbols(t);
    e && (o = o.filter(function(r) {
      return Object.getOwnPropertyDescriptor(t, r).enumerable;
    })), n.push.apply(n, o);
  }
  return n;
}
function k(t) {
  for (var e = 1; e < arguments.length; e++) {
    var n = arguments[e] != null ? arguments[e] : {};
    e % 2 ? lt(Object(n), !0).forEach(function(o) {
      T(t, o, n[o]);
    }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(t, Object.getOwnPropertyDescriptors(n)) : lt(Object(n)).forEach(function(o) {
      Object.defineProperty(t, o, Object.getOwnPropertyDescriptor(n, o));
    });
  }
  return t;
}
function ye(t, e) {
  if (!(t instanceof e)) throw new TypeError("Cannot call a class as a function");
}
function dn(t, e) {
  for (var n = 0; n < e.length; n++) {
    var o = e[n];
    o.enumerable = o.enumerable || !1, o.configurable = !0, "value" in o && (o.writable = !0), Object.defineProperty(t, It(o.key), o);
  }
}
function ve(t, e, n) {
  return e && dn(t.prototype, e), Object.defineProperty(t, "prototype", {
    writable: !1
  }), t;
}
function De(t, e) {
  return De = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function(n, o) {
    return n.__proto__ = o, n;
  }, De(t, e);
}
function jt(t, e) {
  if (typeof e != "function" && e !== null) throw new TypeError("Super expression must either be null or a function");
  t.prototype = Object.create(e && e.prototype, {
    constructor: {
      value: t,
      writable: !0,
      configurable: !0
    }
  }), Object.defineProperty(t, "prototype", {
    writable: !1
  }), e && De(t, e);
}
function se(t) {
  return se = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function(e) {
    return e.__proto__ || Object.getPrototypeOf(e);
  }, se(t);
}
function kt() {
  try {
    var t = !Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function() {
    }));
  } catch {
  }
  return (kt = function() {
    return !!t;
  })();
}
function q(t) {
  if (t === void 0) throw new ReferenceError("this hasn't been initialised - super() hasn't been called");
  return t;
}
function hn(t, e) {
  if (e && (A(e) == "object" || typeof e == "function")) return e;
  if (e !== void 0) throw new TypeError("Derived constructors may only return object or undefined");
  return q(t);
}
function Lt(t) {
  var e = kt();
  return function() {
    var n, o = se(t);
    if (e) {
      var r = se(this).constructor;
      n = Reflect.construct(o, arguments, r);
    } else n = o.apply(this, arguments);
    return hn(this, n);
  };
}
var Rt = /* @__PURE__ */ ve(function t() {
  ye(this, t);
}), Dt = "CALC_UNIT", gn = new RegExp(Dt, "g");
function we(t) {
  return typeof t == "number" ? "".concat(t).concat(Dt) : t;
}
var pn = /* @__PURE__ */ function(t) {
  jt(n, t);
  var e = Lt(n);
  function n(o, r) {
    var i;
    ye(this, n), i = e.call(this), T(q(i), "result", ""), T(q(i), "unitlessCssVar", void 0), T(q(i), "lowPriority", void 0);
    var s = A(o);
    return i.unitlessCssVar = r, o instanceof n ? i.result = "(".concat(o.result, ")") : s === "number" ? i.result = we(o) : s === "string" && (i.result = o), i;
  }
  return ve(n, [{
    key: "add",
    value: function(r) {
      return r instanceof n ? this.result = "".concat(this.result, " + ").concat(r.getResult()) : (typeof r == "number" || typeof r == "string") && (this.result = "".concat(this.result, " + ").concat(we(r))), this.lowPriority = !0, this;
    }
  }, {
    key: "sub",
    value: function(r) {
      return r instanceof n ? this.result = "".concat(this.result, " - ").concat(r.getResult()) : (typeof r == "number" || typeof r == "string") && (this.result = "".concat(this.result, " - ").concat(we(r))), this.lowPriority = !0, this;
    }
  }, {
    key: "mul",
    value: function(r) {
      return this.lowPriority && (this.result = "(".concat(this.result, ")")), r instanceof n ? this.result = "".concat(this.result, " * ").concat(r.getResult(!0)) : (typeof r == "number" || typeof r == "string") && (this.result = "".concat(this.result, " * ").concat(r)), this.lowPriority = !1, this;
    }
  }, {
    key: "div",
    value: function(r) {
      return this.lowPriority && (this.result = "(".concat(this.result, ")")), r instanceof n ? this.result = "".concat(this.result, " / ").concat(r.getResult(!0)) : (typeof r == "number" || typeof r == "string") && (this.result = "".concat(this.result, " / ").concat(r)), this.lowPriority = !1, this;
    }
  }, {
    key: "getResult",
    value: function(r) {
      return this.lowPriority || r ? "(".concat(this.result, ")") : this.result;
    }
  }, {
    key: "equal",
    value: function(r) {
      var i = this, s = r || {}, a = s.unit, l = !0;
      return typeof a == "boolean" ? l = a : Array.from(this.unitlessCssVar).some(function(c) {
        return i.result.includes(c);
      }) && (l = !1), this.result = this.result.replace(gn, l ? "px" : ""), typeof this.lowPriority < "u" ? "calc(".concat(this.result, ")") : this.result;
    }
  }]), n;
}(Rt), mn = /* @__PURE__ */ function(t) {
  jt(n, t);
  var e = Lt(n);
  function n(o) {
    var r;
    return ye(this, n), r = e.call(this), T(q(r), "result", 0), o instanceof n ? r.result = o.result : typeof o == "number" && (r.result = o), r;
  }
  return ve(n, [{
    key: "add",
    value: function(r) {
      return r instanceof n ? this.result += r.result : typeof r == "number" && (this.result += r), this;
    }
  }, {
    key: "sub",
    value: function(r) {
      return r instanceof n ? this.result -= r.result : typeof r == "number" && (this.result -= r), this;
    }
  }, {
    key: "mul",
    value: function(r) {
      return r instanceof n ? this.result *= r.result : typeof r == "number" && (this.result *= r), this;
    }
  }, {
    key: "div",
    value: function(r) {
      return r instanceof n ? this.result /= r.result : typeof r == "number" && (this.result /= r), this;
    }
  }, {
    key: "equal",
    value: function() {
      return this.result;
    }
  }]), n;
}(Rt), bn = function(e, n) {
  var o = e === "css" ? pn : mn;
  return function(r) {
    return new o(r, n);
  };
}, ct = function(e, n) {
  return "".concat([n, e.replace(/([A-Z]+)([A-Z][a-z]+)/g, "$1-$2").replace(/([a-z])([A-Z])/g, "$1-$2")].filter(Boolean).join("-"));
};
function ut(t, e, n, o) {
  var r = k({}, e[t]);
  if (o != null && o.deprecatedTokens) {
    var i = o.deprecatedTokens;
    i.forEach(function(a) {
      var l = N(a, 2), c = l[0], f = l[1];
      if (r != null && r[c] || r != null && r[f]) {
        var u;
        (u = r[f]) !== null && u !== void 0 || (r[f] = r == null ? void 0 : r[c]);
      }
    });
  }
  var s = k(k({}, n), r);
  return Object.keys(s).forEach(function(a) {
    s[a] === e[a] && delete s[a];
  }), s;
}
var Ht = typeof CSSINJS_STATISTIC < "u", He = !0;
function Be() {
  for (var t = arguments.length, e = new Array(t), n = 0; n < t; n++)
    e[n] = arguments[n];
  if (!Ht)
    return Object.assign.apply(Object, [{}].concat(e));
  He = !1;
  var o = {};
  return e.forEach(function(r) {
    if (A(r) === "object") {
      var i = Object.keys(r);
      i.forEach(function(s) {
        Object.defineProperty(o, s, {
          configurable: !0,
          enumerable: !0,
          get: function() {
            return r[s];
          }
        });
      });
    }
  }), He = !0, o;
}
var ft = {};
function yn() {
}
var vn = function(e) {
  var n, o = e, r = yn;
  return Ht && typeof Proxy < "u" && (n = /* @__PURE__ */ new Set(), o = new Proxy(e, {
    get: function(s, a) {
      if (He) {
        var l;
        (l = n) === null || l === void 0 || l.add(a);
      }
      return s[a];
    }
  }), r = function(s, a) {
    var l;
    ft[s] = {
      global: Array.from(n),
      component: k(k({}, (l = ft[s]) === null || l === void 0 ? void 0 : l.component), a)
    };
  }), {
    token: o,
    keys: n,
    flush: r
  };
};
function dt(t, e, n) {
  if (typeof n == "function") {
    var o;
    return n(Be(e, (o = e[t]) !== null && o !== void 0 ? o : {}));
  }
  return n ?? {};
}
function xn(t) {
  return t === "js" ? {
    max: Math.max,
    min: Math.min
  } : {
    max: function() {
      for (var n = arguments.length, o = new Array(n), r = 0; r < n; r++)
        o[r] = arguments[r];
      return "max(".concat(o.map(function(i) {
        return ne(i);
      }).join(","), ")");
    },
    min: function() {
      for (var n = arguments.length, o = new Array(n), r = 0; r < n; r++)
        o[r] = arguments[r];
      return "min(".concat(o.map(function(i) {
        return ne(i);
      }).join(","), ")");
    }
  };
}
var Sn = 1e3 * 60 * 10, Cn = /* @__PURE__ */ function() {
  function t() {
    ye(this, t), T(this, "map", /* @__PURE__ */ new Map()), T(this, "objectIDMap", /* @__PURE__ */ new WeakMap()), T(this, "nextID", 0), T(this, "lastAccessBeat", /* @__PURE__ */ new Map()), T(this, "accessBeat", 0);
  }
  return ve(t, [{
    key: "set",
    value: function(n, o) {
      this.clear();
      var r = this.getCompositeKey(n);
      this.map.set(r, o), this.lastAccessBeat.set(r, Date.now());
    }
  }, {
    key: "get",
    value: function(n) {
      var o = this.getCompositeKey(n), r = this.map.get(o);
      return this.lastAccessBeat.set(o, Date.now()), this.accessBeat += 1, r;
    }
  }, {
    key: "getCompositeKey",
    value: function(n) {
      var o = this, r = n.map(function(i) {
        return i && A(i) === "object" ? "obj_".concat(o.getObjectID(i)) : "".concat(A(i), "_").concat(i);
      });
      return r.join("|");
    }
  }, {
    key: "getObjectID",
    value: function(n) {
      if (this.objectIDMap.has(n))
        return this.objectIDMap.get(n);
      var o = this.nextID;
      return this.objectIDMap.set(n, o), this.nextID += 1, o;
    }
  }, {
    key: "clear",
    value: function() {
      var n = this;
      if (this.accessBeat > 1e4) {
        var o = Date.now();
        this.lastAccessBeat.forEach(function(r, i) {
          o - r > Sn && (n.map.delete(i), n.lastAccessBeat.delete(i));
        }), this.accessBeat = 0;
      }
    }
  }]), t;
}(), ht = new Cn();
function _n(t, e) {
  return b.useMemo(function() {
    var n = ht.get(e);
    if (n)
      return n;
    var o = t();
    return ht.set(e, o), o;
  }, e);
}
var wn = function() {
  return {};
};
function On(t) {
  var e = t.useCSP, n = e === void 0 ? wn : e, o = t.useToken, r = t.usePrefix, i = t.getResetStyles, s = t.getCommonStyle, a = t.getCompUnitless;
  function l(d, g, y, h) {
    var m = Array.isArray(d) ? d[0] : d;
    function v(M) {
      return "".concat(String(m)).concat(M.slice(0, 1).toUpperCase()).concat(M.slice(1));
    }
    var S = (h == null ? void 0 : h.unitless) || {}, E = typeof a == "function" ? a(d) : {}, p = k(k({}, E), {}, T({}, v("zIndexPopup"), !0));
    Object.keys(S).forEach(function(M) {
      p[v(M)] = S[M];
    });
    var C = k(k({}, h), {}, {
      unitless: p,
      prefixToken: v
    }), x = f(d, g, y, C), O = c(m, y, C);
    return function(M) {
      var P = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : M, L = x(M, P), $ = N(L, 2), _ = $[1], z = O(P), j = N(z, 2), R = j[0], B = j[1];
      return [R, _, B];
    };
  }
  function c(d, g, y) {
    var h = y.unitless, m = y.injectStyle, v = m === void 0 ? !0 : m, S = y.prefixToken, E = y.ignore, p = function(O) {
      var M = O.rootCls, P = O.cssVar, L = P === void 0 ? {} : P, $ = o(), _ = $.realToken;
      return sr({
        path: [d],
        prefix: L.prefix,
        key: L.key,
        unitless: h,
        ignore: E,
        token: _,
        scope: M
      }, function() {
        var z = dt(d, _, g), j = ut(d, _, z, {
          deprecatedTokens: y == null ? void 0 : y.deprecatedTokens
        });
        return Object.keys(z).forEach(function(R) {
          j[S(R)] = j[R], delete j[R];
        }), j;
      }), null;
    }, C = function(O) {
      var M = o(), P = M.cssVar;
      return [function(L) {
        return v && P ? /* @__PURE__ */ b.createElement(b.Fragment, null, /* @__PURE__ */ b.createElement(p, {
          rootCls: O,
          cssVar: P,
          component: d
        }), L) : L;
      }, P == null ? void 0 : P.key];
    };
    return C;
  }
  function f(d, g, y) {
    var h = arguments.length > 3 && arguments[3] !== void 0 ? arguments[3] : {}, m = Array.isArray(d) ? d : [d, d], v = N(m, 1), S = v[0], E = m.join("-"), p = t.layer || {
      name: "antd"
    };
    return function(C) {
      var x = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : C, O = o(), M = O.theme, P = O.realToken, L = O.hashId, $ = O.token, _ = O.cssVar, z = r(), j = z.rootPrefixCls, R = z.iconPrefixCls, B = n(), W = _ ? "css" : "js", Bt = _n(function() {
        var V = /* @__PURE__ */ new Set();
        return _ && Object.keys(h.unitless || {}).forEach(function(Q) {
          V.add(xe(Q, _.prefix)), V.add(xe(Q, ct(S, _.prefix)));
        }), bn(W, V);
      }, [W, S, _ == null ? void 0 : _.prefix]), Xe = xn(W), Xt = Xe.max, Ft = Xe.min, Fe = {
        theme: M,
        token: $,
        hashId: L,
        nonce: function() {
          return B.nonce;
        },
        clientOnly: h.clientOnly,
        layer: p,
        // antd is always at top of styles
        order: h.order || -999
      };
      typeof i == "function" && Ue(k(k({}, Fe), {}, {
        clientOnly: !1,
        path: ["Shared", j]
      }), function() {
        return i($, {
          prefix: {
            rootPrefixCls: j,
            iconPrefixCls: R
          },
          csp: B
        });
      });
      var Vt = Ue(k(k({}, Fe), {}, {
        path: [E, C, R]
      }), function() {
        if (h.injectStyle === !1)
          return [];
        var V = vn($), Q = V.token, Nt = V.flush, G = dt(S, P, y), Gt = ".".concat(C), Ve = ut(S, P, G, {
          deprecatedTokens: h.deprecatedTokens
        });
        _ && G && A(G) === "object" && Object.keys(G).forEach(function(Ge) {
          G[Ge] = "var(".concat(xe(Ge, ct(S, _.prefix)), ")");
        });
        var Ne = Be(Q, {
          componentCls: Gt,
          prefixCls: C,
          iconCls: ".".concat(R),
          antCls: ".".concat(j),
          calc: Bt,
          // @ts-ignore
          max: Xt,
          // @ts-ignore
          min: Ft
        }, _ ? G : Ve), Ut = g(Ne, {
          hashId: L,
          prefixCls: C,
          rootPrefixCls: j,
          iconPrefixCls: R
        });
        Nt(S, Ve);
        var Wt = typeof s == "function" ? s(Ne, C, x, h.resetFont) : null;
        return [h.resetStyle === !1 ? null : Wt, Ut];
      });
      return [Vt, L];
    };
  }
  function u(d, g, y) {
    var h = arguments.length > 3 && arguments[3] !== void 0 ? arguments[3] : {}, m = f(d, g, y, k({
      resetStyle: !1,
      // Sub Style should default after root one
      order: -998
    }, h)), v = function(E) {
      var p = E.prefixCls, C = E.rootCls, x = C === void 0 ? p : C;
      return m(p, x), null;
    };
    return v;
  }
  return {
    genStyleHooks: l,
    genSubStyleComponent: u,
    genComponentStyleHook: f
  };
}
const I = Math.round;
function Oe(t, e) {
  const n = t.replace(/^[^(]*\((.*)/, "$1").replace(/\).*/, "").match(/\d*\.?\d+%?/g) || [], o = n.map((r) => parseFloat(r));
  for (let r = 0; r < 3; r += 1)
    o[r] = e(o[r] || 0, n[r] || "", r);
  return n[3] ? o[3] = n[3].includes("%") ? o[3] / 100 : o[3] : o[3] = 1, o;
}
const gt = (t, e, n) => n === 0 ? t : t / 100;
function K(t, e) {
  const n = e || 255;
  return t > n ? n : t < 0 ? 0 : t;
}
class X {
  constructor(e) {
    T(this, "isValid", !0), T(this, "r", 0), T(this, "g", 0), T(this, "b", 0), T(this, "a", 1), T(this, "_h", void 0), T(this, "_s", void 0), T(this, "_l", void 0), T(this, "_v", void 0), T(this, "_max", void 0), T(this, "_min", void 0), T(this, "_brightness", void 0);
    function n(o) {
      return o[0] in e && o[1] in e && o[2] in e;
    }
    if (e) if (typeof e == "string") {
      let r = function(i) {
        return o.startsWith(i);
      };
      const o = e.trim();
      /^#?[A-F\d]{3,8}$/i.test(o) ? this.fromHexString(o) : r("rgb") ? this.fromRgbString(o) : r("hsl") ? this.fromHslString(o) : (r("hsv") || r("hsb")) && this.fromHsvString(o);
    } else if (e instanceof X)
      this.r = e.r, this.g = e.g, this.b = e.b, this.a = e.a, this._h = e._h, this._s = e._s, this._l = e._l, this._v = e._v;
    else if (n("rgb"))
      this.r = K(e.r), this.g = K(e.g), this.b = K(e.b), this.a = typeof e.a == "number" ? K(e.a, 1) : 1;
    else if (n("hsl"))
      this.fromHsl(e);
    else if (n("hsv"))
      this.fromHsv(e);
    else
      throw new Error("@ant-design/fast-color: unsupported input " + JSON.stringify(e));
  }
  // ======================= Setter =======================
  setR(e) {
    return this._sc("r", e);
  }
  setG(e) {
    return this._sc("g", e);
  }
  setB(e) {
    return this._sc("b", e);
  }
  setA(e) {
    return this._sc("a", e, 1);
  }
  setHue(e) {
    const n = this.toHsv();
    return n.h = e, this._c(n);
  }
  // ======================= Getter =======================
  /**
   * Returns the perceived luminance of a color, from 0-1.
   * @see http://www.w3.org/TR/2008/REC-WCAG20-20081211/#relativeluminancedef
   */
  getLuminance() {
    function e(i) {
      const s = i / 255;
      return s <= 0.03928 ? s / 12.92 : Math.pow((s + 0.055) / 1.055, 2.4);
    }
    const n = e(this.r), o = e(this.g), r = e(this.b);
    return 0.2126 * n + 0.7152 * o + 0.0722 * r;
  }
  getHue() {
    if (typeof this._h > "u") {
      const e = this.getMax() - this.getMin();
      e === 0 ? this._h = 0 : this._h = I(60 * (this.r === this.getMax() ? (this.g - this.b) / e + (this.g < this.b ? 6 : 0) : this.g === this.getMax() ? (this.b - this.r) / e + 2 : (this.r - this.g) / e + 4));
    }
    return this._h;
  }
  getSaturation() {
    if (typeof this._s > "u") {
      const e = this.getMax() - this.getMin();
      e === 0 ? this._s = 0 : this._s = e / this.getMax();
    }
    return this._s;
  }
  getLightness() {
    return typeof this._l > "u" && (this._l = (this.getMax() + this.getMin()) / 510), this._l;
  }
  getValue() {
    return typeof this._v > "u" && (this._v = this.getMax() / 255), this._v;
  }
  /**
   * Returns the perceived brightness of the color, from 0-255.
   * Note: this is not the b of HSB
   * @see http://www.w3.org/TR/AERT#color-contrast
   */
  getBrightness() {
    return typeof this._brightness > "u" && (this._brightness = (this.r * 299 + this.g * 587 + this.b * 114) / 1e3), this._brightness;
  }
  // ======================== Func ========================
  darken(e = 10) {
    const n = this.getHue(), o = this.getSaturation();
    let r = this.getLightness() - e / 100;
    return r < 0 && (r = 0), this._c({
      h: n,
      s: o,
      l: r,
      a: this.a
    });
  }
  lighten(e = 10) {
    const n = this.getHue(), o = this.getSaturation();
    let r = this.getLightness() + e / 100;
    return r > 1 && (r = 1), this._c({
      h: n,
      s: o,
      l: r,
      a: this.a
    });
  }
  /**
   * Mix the current color a given amount with another color, from 0 to 100.
   * 0 means no mixing (return current color).
   */
  mix(e, n = 50) {
    const o = this._c(e), r = n / 100, i = (a) => (o[a] - this[a]) * r + this[a], s = {
      r: I(i("r")),
      g: I(i("g")),
      b: I(i("b")),
      a: I(i("a") * 100) / 100
    };
    return this._c(s);
  }
  /**
   * Mix the color with pure white, from 0 to 100.
   * Providing 0 will do nothing, providing 100 will always return white.
   */
  tint(e = 10) {
    return this.mix({
      r: 255,
      g: 255,
      b: 255,
      a: 1
    }, e);
  }
  /**
   * Mix the color with pure black, from 0 to 100.
   * Providing 0 will do nothing, providing 100 will always return black.
   */
  shade(e = 10) {
    return this.mix({
      r: 0,
      g: 0,
      b: 0,
      a: 1
    }, e);
  }
  onBackground(e) {
    const n = this._c(e), o = this.a + n.a * (1 - this.a), r = (i) => I((this[i] * this.a + n[i] * n.a * (1 - this.a)) / o);
    return this._c({
      r: r("r"),
      g: r("g"),
      b: r("b"),
      a: o
    });
  }
  // ======================= Status =======================
  isDark() {
    return this.getBrightness() < 128;
  }
  isLight() {
    return this.getBrightness() >= 128;
  }
  // ======================== MISC ========================
  equals(e) {
    return this.r === e.r && this.g === e.g && this.b === e.b && this.a === e.a;
  }
  clone() {
    return this._c(this);
  }
  // ======================= Format =======================
  toHexString() {
    let e = "#";
    const n = (this.r || 0).toString(16);
    e += n.length === 2 ? n : "0" + n;
    const o = (this.g || 0).toString(16);
    e += o.length === 2 ? o : "0" + o;
    const r = (this.b || 0).toString(16);
    if (e += r.length === 2 ? r : "0" + r, typeof this.a == "number" && this.a >= 0 && this.a < 1) {
      const i = I(this.a * 255).toString(16);
      e += i.length === 2 ? i : "0" + i;
    }
    return e;
  }
  /** CSS support color pattern */
  toHsl() {
    return {
      h: this.getHue(),
      s: this.getSaturation(),
      l: this.getLightness(),
      a: this.a
    };
  }
  /** CSS support color pattern */
  toHslString() {
    const e = this.getHue(), n = I(this.getSaturation() * 100), o = I(this.getLightness() * 100);
    return this.a !== 1 ? `hsla(${e},${n}%,${o}%,${this.a})` : `hsl(${e},${n}%,${o}%)`;
  }
  /** Same as toHsb */
  toHsv() {
    return {
      h: this.getHue(),
      s: this.getSaturation(),
      v: this.getValue(),
      a: this.a
    };
  }
  toRgb() {
    return {
      r: this.r,
      g: this.g,
      b: this.b,
      a: this.a
    };
  }
  toRgbString() {
    return this.a !== 1 ? `rgba(${this.r},${this.g},${this.b},${this.a})` : `rgb(${this.r},${this.g},${this.b})`;
  }
  toString() {
    return this.toRgbString();
  }
  // ====================== Privates ======================
  /** Return a new FastColor object with one channel changed */
  _sc(e, n, o) {
    const r = this.clone();
    return r[e] = K(n, o), r;
  }
  _c(e) {
    return new this.constructor(e);
  }
  getMax() {
    return typeof this._max > "u" && (this._max = Math.max(this.r, this.g, this.b)), this._max;
  }
  getMin() {
    return typeof this._min > "u" && (this._min = Math.min(this.r, this.g, this.b)), this._min;
  }
  fromHexString(e) {
    const n = e.replace("#", "");
    function o(r, i) {
      return parseInt(n[r] + n[i || r], 16);
    }
    n.length < 6 ? (this.r = o(0), this.g = o(1), this.b = o(2), this.a = n[3] ? o(3) / 255 : 1) : (this.r = o(0, 1), this.g = o(2, 3), this.b = o(4, 5), this.a = n[6] ? o(6, 7) / 255 : 1);
  }
  fromHsl({
    h: e,
    s: n,
    l: o,
    a: r
  }) {
    if (this._h = e % 360, this._s = n, this._l = o, this.a = typeof r == "number" ? r : 1, n <= 0) {
      const d = I(o * 255);
      this.r = d, this.g = d, this.b = d;
    }
    let i = 0, s = 0, a = 0;
    const l = e / 60, c = (1 - Math.abs(2 * o - 1)) * n, f = c * (1 - Math.abs(l % 2 - 1));
    l >= 0 && l < 1 ? (i = c, s = f) : l >= 1 && l < 2 ? (i = f, s = c) : l >= 2 && l < 3 ? (s = c, a = f) : l >= 3 && l < 4 ? (s = f, a = c) : l >= 4 && l < 5 ? (i = f, a = c) : l >= 5 && l < 6 && (i = c, a = f);
    const u = o - c / 2;
    this.r = I((i + u) * 255), this.g = I((s + u) * 255), this.b = I((a + u) * 255);
  }
  fromHsv({
    h: e,
    s: n,
    v: o,
    a: r
  }) {
    this._h = e % 360, this._s = n, this._v = o, this.a = typeof r == "number" ? r : 1;
    const i = I(o * 255);
    if (this.r = i, this.g = i, this.b = i, n <= 0)
      return;
    const s = e / 60, a = Math.floor(s), l = s - a, c = I(o * (1 - n) * 255), f = I(o * (1 - n * l) * 255), u = I(o * (1 - n * (1 - l)) * 255);
    switch (a) {
      case 0:
        this.g = u, this.b = c;
        break;
      case 1:
        this.r = f, this.b = c;
        break;
      case 2:
        this.r = c, this.b = u;
        break;
      case 3:
        this.r = c, this.g = f;
        break;
      case 4:
        this.r = u, this.g = c;
        break;
      case 5:
      default:
        this.g = c, this.b = f;
        break;
    }
  }
  fromHsvString(e) {
    const n = Oe(e, gt);
    this.fromHsv({
      h: n[0],
      s: n[1],
      v: n[2],
      a: n[3]
    });
  }
  fromHslString(e) {
    const n = Oe(e, gt);
    this.fromHsl({
      h: n[0],
      s: n[1],
      l: n[2],
      a: n[3]
    });
  }
  fromRgbString(e) {
    const n = Oe(e, (o, r) => (
      // Convert percentage to number. e.g. 50% -> 128
      r.includes("%") ? I(o / 100 * 255) : o
    ));
    this.r = n[0], this.g = n[1], this.b = n[2], this.a = n[3];
  }
}
const Tn = {
  blue: "#1677FF",
  purple: "#722ED1",
  cyan: "#13C2C2",
  green: "#52C41A",
  magenta: "#EB2F96",
  /**
   * @deprecated Use magenta instead
   */
  pink: "#EB2F96",
  red: "#F5222D",
  orange: "#FA8C16",
  yellow: "#FADB14",
  volcano: "#FA541C",
  geekblue: "#2F54EB",
  gold: "#FAAD14",
  lime: "#A0D911"
}, En = Object.assign(Object.assign({}, Tn), {
  // Color
  colorPrimary: "#1677ff",
  colorSuccess: "#52c41a",
  colorWarning: "#faad14",
  colorError: "#ff4d4f",
  colorInfo: "#1677ff",
  colorLink: "",
  colorTextBase: "",
  colorBgBase: "",
  // Font
  fontFamily: `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial,
'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol',
'Noto Color Emoji'`,
  fontFamilyCode: "'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, Courier, monospace",
  fontSize: 14,
  // Line
  lineWidth: 1,
  lineType: "solid",
  // Motion
  motionUnit: 0.1,
  motionBase: 0,
  motionEaseOutCirc: "cubic-bezier(0.08, 0.82, 0.17, 1)",
  motionEaseInOutCirc: "cubic-bezier(0.78, 0.14, 0.15, 0.86)",
  motionEaseOut: "cubic-bezier(0.215, 0.61, 0.355, 1)",
  motionEaseInOut: "cubic-bezier(0.645, 0.045, 0.355, 1)",
  motionEaseOutBack: "cubic-bezier(0.12, 0.4, 0.29, 1.46)",
  motionEaseInBack: "cubic-bezier(0.71, -0.46, 0.88, 0.6)",
  motionEaseInQuint: "cubic-bezier(0.755, 0.05, 0.855, 0.06)",
  motionEaseOutQuint: "cubic-bezier(0.23, 1, 0.32, 1)",
  // Radius
  borderRadius: 6,
  // Size
  sizeUnit: 4,
  sizeStep: 4,
  sizePopupArrow: 16,
  // Control Base
  controlHeight: 32,
  // zIndex
  zIndexBase: 0,
  zIndexPopupBase: 1e3,
  // Image
  opacityImage: 1,
  // Wireframe
  wireframe: !1,
  // Motion
  motion: !0
});
function Te(t) {
  return t >= 0 && t <= 255;
}
function J(t, e) {
  const {
    r: n,
    g: o,
    b: r,
    a: i
  } = new X(t).toRgb();
  if (i < 1)
    return t;
  const {
    r: s,
    g: a,
    b: l
  } = new X(e).toRgb();
  for (let c = 0.01; c <= 1; c += 0.01) {
    const f = Math.round((n - s * (1 - c)) / c), u = Math.round((o - a * (1 - c)) / c), d = Math.round((r - l * (1 - c)) / c);
    if (Te(f) && Te(u) && Te(d))
      return new X({
        r: f,
        g: u,
        b: d,
        a: Math.round(c * 100) / 100
      }).toRgbString();
  }
  return new X({
    r: n,
    g: o,
    b: r,
    a: 1
  }).toRgbString();
}
var Mn = function(t, e) {
  var n = {};
  for (var o in t) Object.prototype.hasOwnProperty.call(t, o) && e.indexOf(o) < 0 && (n[o] = t[o]);
  if (t != null && typeof Object.getOwnPropertySymbols == "function") for (var r = 0, o = Object.getOwnPropertySymbols(t); r < o.length; r++)
    e.indexOf(o[r]) < 0 && Object.prototype.propertyIsEnumerable.call(t, o[r]) && (n[o[r]] = t[o[r]]);
  return n;
};
function Pn(t) {
  const {
    override: e
  } = t, n = Mn(t, ["override"]), o = Object.assign({}, e);
  Object.keys(En).forEach((d) => {
    delete o[d];
  });
  const r = Object.assign(Object.assign({}, n), o), i = 480, s = 576, a = 768, l = 992, c = 1200, f = 1600;
  if (r.motion === !1) {
    const d = "0s";
    r.motionDurationFast = d, r.motionDurationMid = d, r.motionDurationSlow = d;
  }
  return Object.assign(Object.assign(Object.assign({}, r), {
    // ============== Background ============== //
    colorFillContent: r.colorFillSecondary,
    colorFillContentHover: r.colorFill,
    colorFillAlter: r.colorFillQuaternary,
    colorBgContainerDisabled: r.colorFillTertiary,
    // ============== Split ============== //
    colorBorderBg: r.colorBgContainer,
    colorSplit: J(r.colorBorderSecondary, r.colorBgContainer),
    // ============== Text ============== //
    colorTextPlaceholder: r.colorTextQuaternary,
    colorTextDisabled: r.colorTextQuaternary,
    colorTextHeading: r.colorText,
    colorTextLabel: r.colorTextSecondary,
    colorTextDescription: r.colorTextTertiary,
    colorTextLightSolid: r.colorWhite,
    colorHighlight: r.colorError,
    colorBgTextHover: r.colorFillSecondary,
    colorBgTextActive: r.colorFill,
    colorIcon: r.colorTextTertiary,
    colorIconHover: r.colorText,
    colorErrorOutline: J(r.colorErrorBg, r.colorBgContainer),
    colorWarningOutline: J(r.colorWarningBg, r.colorBgContainer),
    // Font
    fontSizeIcon: r.fontSizeSM,
    // Line
    lineWidthFocus: r.lineWidth * 3,
    // Control
    lineWidth: r.lineWidth,
    controlOutlineWidth: r.lineWidth * 2,
    // Checkbox size and expand icon size
    controlInteractiveSize: r.controlHeight / 2,
    controlItemBgHover: r.colorFillTertiary,
    controlItemBgActive: r.colorPrimaryBg,
    controlItemBgActiveHover: r.colorPrimaryBgHover,
    controlItemBgActiveDisabled: r.colorFill,
    controlTmpOutline: r.colorFillQuaternary,
    controlOutline: J(r.colorPrimaryBg, r.colorBgContainer),
    lineType: r.lineType,
    borderRadius: r.borderRadius,
    borderRadiusXS: r.borderRadiusXS,
    borderRadiusSM: r.borderRadiusSM,
    borderRadiusLG: r.borderRadiusLG,
    fontWeightStrong: 600,
    opacityLoading: 0.65,
    linkDecoration: "none",
    linkHoverDecoration: "none",
    linkFocusDecoration: "none",
    controlPaddingHorizontal: 12,
    controlPaddingHorizontalSM: 8,
    paddingXXS: r.sizeXXS,
    paddingXS: r.sizeXS,
    paddingSM: r.sizeSM,
    padding: r.size,
    paddingMD: r.sizeMD,
    paddingLG: r.sizeLG,
    paddingXL: r.sizeXL,
    paddingContentHorizontalLG: r.sizeLG,
    paddingContentVerticalLG: r.sizeMS,
    paddingContentHorizontal: r.sizeMS,
    paddingContentVertical: r.sizeSM,
    paddingContentHorizontalSM: r.size,
    paddingContentVerticalSM: r.sizeXS,
    marginXXS: r.sizeXXS,
    marginXS: r.sizeXS,
    marginSM: r.sizeSM,
    margin: r.size,
    marginMD: r.sizeMD,
    marginLG: r.sizeLG,
    marginXL: r.sizeXL,
    marginXXL: r.sizeXXL,
    boxShadow: `
      0 6px 16px 0 rgba(0, 0, 0, 0.08),
      0 3px 6px -4px rgba(0, 0, 0, 0.12),
      0 9px 28px 8px rgba(0, 0, 0, 0.05)
    `,
    boxShadowSecondary: `
      0 6px 16px 0 rgba(0, 0, 0, 0.08),
      0 3px 6px -4px rgba(0, 0, 0, 0.12),
      0 9px 28px 8px rgba(0, 0, 0, 0.05)
    `,
    boxShadowTertiary: `
      0 1px 2px 0 rgba(0, 0, 0, 0.03),
      0 1px 6px -1px rgba(0, 0, 0, 0.02),
      0 2px 4px 0 rgba(0, 0, 0, 0.02)
    `,
    screenXS: i,
    screenXSMin: i,
    screenXSMax: s - 1,
    screenSM: s,
    screenSMMin: s,
    screenSMMax: a - 1,
    screenMD: a,
    screenMDMin: a,
    screenMDMax: l - 1,
    screenLG: l,
    screenLGMin: l,
    screenLGMax: c - 1,
    screenXL: c,
    screenXLMin: c,
    screenXLMax: f - 1,
    screenXXL: f,
    screenXXLMin: f,
    boxShadowPopoverArrow: "2px 2px 5px rgba(0, 0, 0, 0.05)",
    boxShadowCard: `
      0 1px 2px -2px ${new X("rgba(0, 0, 0, 0.16)").toRgbString()},
      0 3px 6px 0 ${new X("rgba(0, 0, 0, 0.12)").toRgbString()},
      0 5px 12px 4px ${new X("rgba(0, 0, 0, 0.09)").toRgbString()}
    `,
    boxShadowDrawerRight: `
      -6px 0 16px 0 rgba(0, 0, 0, 0.08),
      -3px 0 6px -4px rgba(0, 0, 0, 0.12),
      -9px 0 28px 8px rgba(0, 0, 0, 0.05)
    `,
    boxShadowDrawerLeft: `
      6px 0 16px 0 rgba(0, 0, 0, 0.08),
      3px 0 6px -4px rgba(0, 0, 0, 0.12),
      9px 0 28px 8px rgba(0, 0, 0, 0.05)
    `,
    boxShadowDrawerUp: `
      0 6px 16px 0 rgba(0, 0, 0, 0.08),
      0 3px 6px -4px rgba(0, 0, 0, 0.12),
      0 9px 28px 8px rgba(0, 0, 0, 0.05)
    `,
    boxShadowDrawerDown: `
      0 -6px 16px 0 rgba(0, 0, 0, 0.08),
      0 -3px 6px -4px rgba(0, 0, 0, 0.12),
      0 -9px 28px 8px rgba(0, 0, 0, 0.05)
    `,
    boxShadowTabsOverflowLeft: "inset 10px 0 8px -8px rgba(0, 0, 0, 0.08)",
    boxShadowTabsOverflowRight: "inset -10px 0 8px -8px rgba(0, 0, 0, 0.08)",
    boxShadowTabsOverflowTop: "inset 0 10px 8px -8px rgba(0, 0, 0, 0.08)",
    boxShadowTabsOverflowBottom: "inset 0 -10px 8px -8px rgba(0, 0, 0, 0.08)"
  }), o);
}
const In = {
  lineHeight: !0,
  lineHeightSM: !0,
  lineHeightLG: !0,
  lineHeightHeading1: !0,
  lineHeightHeading2: !0,
  lineHeightHeading3: !0,
  lineHeightHeading4: !0,
  lineHeightHeading5: !0,
  opacityLoading: !0,
  fontWeightStrong: !0,
  zIndexPopupBase: !0,
  zIndexBase: !0,
  opacityImage: !0
}, jn = {
  size: !0,
  sizeSM: !0,
  sizeLG: !0,
  sizeMD: !0,
  sizeXS: !0,
  sizeXXS: !0,
  sizeMS: !0,
  sizeXL: !0,
  sizeXXL: !0,
  sizeUnit: !0,
  sizeStep: !0,
  motionBase: !0,
  motionUnit: !0
}, kn = ar(je.defaultAlgorithm), Ln = {
  screenXS: !0,
  screenXSMin: !0,
  screenXSMax: !0,
  screenSM: !0,
  screenSMMin: !0,
  screenSMMax: !0,
  screenMD: !0,
  screenMDMin: !0,
  screenMDMax: !0,
  screenLG: !0,
  screenLGMin: !0,
  screenLGMax: !0,
  screenXL: !0,
  screenXLMin: !0,
  screenXLMax: !0,
  screenXXL: !0,
  screenXXLMin: !0
}, At = (t, e, n) => {
  const o = n.getDerivativeToken(t), {
    override: r,
    ...i
  } = e;
  let s = {
    ...o,
    override: r
  };
  return s = Pn(s), i && Object.entries(i).forEach(([a, l]) => {
    const {
      theme: c,
      ...f
    } = l;
    let u = f;
    c && (u = At({
      ...s,
      ...f
    }, {
      override: f
    }, c)), s[a] = u;
  }), s;
};
function Rn() {
  const {
    token: t,
    hashed: e,
    theme: n = kn,
    override: o,
    cssVar: r
  } = b.useContext(je._internalContext), [i, s, a] = lr(n, [je.defaultSeed, t], {
    salt: `${Jr}-${e || ""}`,
    override: o,
    getComputedToken: At,
    cssVar: r && {
      prefix: r.prefix,
      key: r.key,
      unitless: In,
      ignore: jn,
      preserve: Ln
    }
  });
  return [n, a, e ? s : "", i, r];
}
const {
  genStyleHooks: Dn,
  genComponentStyleHook: no,
  genSubStyleComponent: oo
} = On({
  usePrefix: () => {
    const {
      getPrefixCls: t,
      iconPrefixCls: e
    } = Re();
    return {
      iconPrefixCls: e,
      rootPrefixCls: t()
    };
  },
  useToken: () => {
    const [t, e, n, o, r] = Rn();
    return {
      theme: t,
      realToken: e,
      hashId: n,
      token: o,
      cssVar: r
    };
  },
  useCSP: () => {
    const {
      csp: t
    } = Re();
    return t ?? {};
  },
  layer: {
    name: "antdx",
    dependencies: ["antd"]
  }
});
var Hn = `accept acceptCharset accessKey action allowFullScreen allowTransparency
    alt async autoComplete autoFocus autoPlay capture cellPadding cellSpacing challenge
    charSet checked classID className colSpan cols content contentEditable contextMenu
    controls coords crossOrigin data dateTime default defer dir disabled download draggable
    encType form formAction formEncType formMethod formNoValidate formTarget frameBorder
    headers height hidden high href hrefLang htmlFor httpEquiv icon id inputMode integrity
    is keyParams keyType kind label lang list loop low manifest marginHeight marginWidth max maxLength media
    mediaGroup method min minLength multiple muted name noValidate nonce open
    optimum pattern placeholder poster preload radioGroup readOnly rel required
    reversed role rowSpan rows sandbox scope scoped scrolling seamless selected
    shape size sizes span spellCheck src srcDoc srcLang srcSet start step style
    summary tabIndex target title type useMap value width wmode wrap`, An = `onCopy onCut onPaste onCompositionEnd onCompositionStart onCompositionUpdate onKeyDown
    onKeyPress onKeyUp onFocus onBlur onChange onInput onSubmit onClick onContextMenu onDoubleClick
    onDrag onDragEnd onDragEnter onDragExit onDragLeave onDragOver onDragStart onDrop onMouseDown
    onMouseEnter onMouseLeave onMouseMove onMouseOut onMouseOver onMouseUp onSelect onTouchCancel
    onTouchEnd onTouchMove onTouchStart onScroll onWheel onAbort onCanPlay onCanPlayThrough
    onDurationChange onEmptied onEncrypted onEnded onError onLoadedData onLoadedMetadata
    onLoadStart onPause onPlay onPlaying onProgress onRateChange onSeeked onSeeking onStalled onSuspend onTimeUpdate onVolumeChange onWaiting onLoad onError`, $n = "".concat(Hn, " ").concat(An).split(/[\s\n]+/), zn = "aria-", Bn = "data-";
function pt(t, e) {
  return t.indexOf(e) === 0;
}
function $t(t) {
  var e = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : !1, n;
  e === !1 ? n = {
    aria: !0,
    data: !0,
    attr: !0
  } : e === !0 ? n = {
    aria: !0
  } : n = k({}, e);
  var o = {};
  return Object.keys(t).forEach(function(r) {
    // Aria
    (n.aria && (r === "role" || pt(r, zn)) || // Data
    n.data && pt(r, Bn) || // Attr
    n.attr && $n.includes(r)) && (o[r] = t[r]);
  }), o;
}
const zt = /* @__PURE__ */ b.createContext(null), mt = ({
  children: t
}) => {
  const {
    prefixCls: e
  } = b.useContext(zt);
  return /* @__PURE__ */ b.createElement("div", {
    className: te(`${e}-group-title`)
  }, t && /* @__PURE__ */ b.createElement(Ct.Text, null, t));
}, Xn = (t) => {
  t.stopPropagation();
}, Fn = (t) => {
  const {
    prefixCls: e,
    info: n,
    className: o,
    direction: r,
    onClick: i,
    active: s,
    menu: a,
    ...l
  } = t, c = $t(l, {
    aria: !0,
    data: !0,
    attr: !0
  }), {
    disabled: f
  } = n, [u, d] = b.useState(!1), [g, y] = b.useState(!1), h = te(o, `${e}-item`, {
    [`${e}-item-active`]: s && !f
  }, {
    [`${e}-item-disabled`]: f
  }), m = () => {
    !f && i && i(n);
  }, v = (S) => {
    S && y(!S);
  };
  return /* @__PURE__ */ b.createElement(nr, {
    title: n.label,
    open: u && g,
    onOpenChange: y,
    placement: r === "rtl" ? "left" : "right"
  }, /* @__PURE__ */ b.createElement("li", ie({}, c, {
    className: h,
    onClick: m
  }), n.icon && /* @__PURE__ */ b.createElement("div", {
    className: `${e}-icon`
  }, n.icon), /* @__PURE__ */ b.createElement(Ct.Text, {
    className: `${e}-label`,
    ellipsis: {
      onEllipsis: d
    }
  }, n.label), a && !f && /* @__PURE__ */ b.createElement(or, {
    menu: a,
    placement: r === "rtl" ? "bottomLeft" : "bottomRight",
    trigger: ["click"],
    disabled: f,
    onOpenChange: v
  }, /* @__PURE__ */ b.createElement(ir, {
    onClick: Xn,
    disabled: f,
    className: `${e}-menu-icon`
  }))));
}, Ee = "__ungrouped", Vn = (t, e = []) => {
  const [n, o, r] = b.useMemo(() => {
    if (!t)
      return [!1, void 0, void 0];
    let i = {
      sort: void 0,
      title: void 0
    };
    return typeof t == "object" && (i = {
      ...i,
      ...t
    }), [!0, i.sort, i.title];
  }, [t]);
  return b.useMemo(() => {
    if (!n)
      return [[{
        name: Ee,
        data: e,
        title: void 0
      }], n];
    const i = e.reduce((l, c) => {
      const f = c.group || Ee;
      return l[f] || (l[f] = []), l[f].push(c), l;
    }, {});
    return [(o ? Object.keys(i).sort(o) : Object.keys(i)).map((l) => ({
      name: l === Ee ? void 0 : l,
      title: r,
      data: i[l]
    })), n];
  }, [e, t]);
}, Nn = (t) => {
  const {
    componentCls: e
  } = t;
  return {
    [e]: {
      display: "flex",
      flexDirection: "column",
      gap: t.paddingXXS,
      overflowY: "auto",
      padding: t.paddingSM,
      [`&${e}-rtl`]: {
        direction: "rtl"
      },
      // 会话列表
      [`& ${e}-list`]: {
        display: "flex",
        gap: t.paddingXXS,
        flexDirection: "column",
        [`& ${e}-item`]: {
          paddingInlineStart: t.paddingXL
        },
        [`& ${e}-label`]: {
          color: t.colorTextDescription
        }
      },
      // 会话列表项
      [`& ${e}-item`]: {
        display: "flex",
        height: t.controlHeightLG,
        minHeight: t.controlHeightLG,
        gap: t.paddingXS,
        padding: `0 ${ne(t.paddingXS)}`,
        alignItems: "center",
        borderRadius: t.borderRadiusLG,
        cursor: "pointer",
        transition: `all ${t.motionDurationMid} ${t.motionEaseInOut}`,
        // 悬浮样式
        "&:hover": {
          backgroundColor: t.colorBgTextHover
        },
        // 选中样式
        "&-active": {
          backgroundColor: t.colorBgTextHover,
          [`& ${e}-label, ${e}-menu-icon`]: {
            color: t.colorText
          }
        },
        // 禁用样式
        "&-disabled": {
          cursor: "not-allowed",
          [`& ${e}-label`]: {
            color: t.colorTextDisabled
          }
        },
        // 悬浮、选中时激活操作菜单
        "&:hover, &-active": {
          [`& ${e}-menu-icon`]: {
            opacity: 1
          }
        }
      },
      // 会话名
      [`& ${e}-label`]: {
        flex: 1,
        color: t.colorText
      },
      // 会话操作菜单
      [`& ${e}-menu-icon`]: {
        opacity: 0,
        fontSize: t.fontSizeXL
      },
      // 会话图标
      [`& ${e}-group-title`]: {
        display: "flex",
        alignItems: "center",
        height: t.controlHeightLG,
        minHeight: t.controlHeightLG,
        padding: `0 ${ne(t.paddingXS)}`
      }
    }
  };
}, Gn = () => ({}), Un = Dn("Conversations", (t) => {
  const e = Be(t, {});
  return Nn(e);
}, Gn), Wn = (t) => {
  const {
    prefixCls: e,
    rootClassName: n,
    items: o,
    activeKey: r,
    defaultActiveKey: i,
    onActiveChange: s,
    menu: a,
    styles: l = {},
    classNames: c = {},
    groupable: f,
    className: u,
    style: d,
    ...g
  } = t, y = $t(g, {
    attr: !0,
    aria: !0,
    data: !0
  }), [h, m] = ln(i, {
    value: r
  }), [v, S] = Vn(f, o), {
    getPrefixCls: E,
    direction: p
  } = Re(), C = E("conversations", e), x = en("conversations"), [O, M, P] = Un(C), L = te(C, x.className, u, n, M, P, {
    [`${C}-rtl`]: p === "rtl"
  }), $ = (_) => {
    m(_.key), s && s(_.key);
  };
  return O(/* @__PURE__ */ b.createElement("ul", ie({}, y, {
    style: {
      ...x.style,
      ...d
    },
    className: L
  }), v.map((_, z) => {
    var R;
    const j = _.data.map((B, W) => /* @__PURE__ */ b.createElement(Fn, {
      key: B.key || `key-${W}`,
      info: B,
      prefixCls: C,
      direction: p,
      className: te(c.item, x.classNames.item),
      style: {
        ...x.styles.item,
        ...l.item
      },
      menu: typeof a == "function" ? a(B) : a,
      active: h === B.key,
      onClick: $
    }));
    return S ? /* @__PURE__ */ b.createElement("li", {
      key: _.name || `key-${z}`
    }, /* @__PURE__ */ b.createElement(zt.Provider, {
      value: {
        prefixCls: C
      }
    }, ((R = _.title) == null ? void 0 : R.call(_, _.name, {
      components: {
        GroupTitle: mt
      }
    })) || /* @__PURE__ */ b.createElement(mt, {
      key: _.name
    }, _.name)), /* @__PURE__ */ b.createElement("ul", {
      className: `${C}-list`
    }, j)) : j;
  })));
};
function Kn(t) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(t.trim());
}
function qn(t, e = !1) {
  try {
    if (xt(t))
      return t;
    if (e && !Kn(t))
      return;
    if (typeof t == "string") {
      let n = t.trim();
      return n.startsWith(";") && (n = n.slice(1)), n.endsWith(";") && (n = n.slice(0, -1)), new Function(`return (...args) => (${n})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function bt(t, e) {
  return Me(() => qn(t, e), [t, e]);
}
function Ae(t, e, n) {
  const o = t.filter(Boolean);
  if (o.length !== 0)
    return o.map((r, i) => {
      var c;
      if (typeof r != "object")
        return e != null && e.fallback ? e.fallback(r) : r;
      const s = {
        ...r.props,
        key: ((c = r.props) == null ? void 0 : c.key) ?? (n ? `${n}-${i}` : `${i}`)
      };
      let a = s;
      Object.keys(r.slots).forEach((f) => {
        if (!r.slots[f] || !(r.slots[f] instanceof Element) && !r.slots[f].el)
          return;
        const u = f.split(".");
        u.forEach((v, S) => {
          a[v] || (a[v] = {}), S !== u.length - 1 && (a = s[v]);
        });
        const d = r.slots[f];
        let g, y, h = (e == null ? void 0 : e.clone) ?? !1, m = e == null ? void 0 : e.forceClone;
        d instanceof Element ? g = d : (g = d.el, y = d.callback, h = d.clone ?? h, m = d.forceClone ?? m), m = m ?? !!y, a[u[u.length - 1]] = g ? y ? (...v) => (y(u[u.length - 1], v), /* @__PURE__ */ D.jsx(re, {
          params: v,
          forceClone: m,
          children: /* @__PURE__ */ D.jsx(oe, {
            slot: g,
            clone: h
          })
        })) : /* @__PURE__ */ D.jsx(re, {
          forceClone: m,
          children: /* @__PURE__ */ D.jsx(oe, {
            slot: g,
            clone: h
          })
        }) : a[u[u.length - 1]], a = s;
      });
      const l = (e == null ? void 0 : e.children) || "children";
      return r[l] ? s[l] = Ae(r[l], e, `${i}`) : e != null && e.children && (s[l] = void 0, Reflect.deleteProperty(s, l)), s;
    });
}
function yt(t, e) {
  return t ? /* @__PURE__ */ D.jsx(oe, {
    slot: t,
    clone: e == null ? void 0 : e.clone
  }) : null;
}
function vt({
  key: t,
  slots: e,
  targets: n
}, o) {
  return e[t] ? (...r) => n ? n.map((i, s) => /* @__PURE__ */ D.jsx(re, {
    params: r,
    forceClone: (o == null ? void 0 : o.forceClone) ?? !0,
    children: yt(i, {
      clone: !0,
      ...o
    })
  }, s)) : /* @__PURE__ */ D.jsx(re, {
    params: r,
    forceClone: (o == null ? void 0 : o.forceClone) ?? !0,
    children: yt(e[t], {
      clone: !0,
      ...o
    })
  }) : void 0;
}
const {
  useItems: Qn,
  withItemsContextProvider: Jn,
  ItemHandler: io
} = St("antd-menu-items"), {
  useItems: Zn,
  withItemsContextProvider: Yn,
  ItemHandler: so
} = St("antdx-conversations-items");
function eo(t) {
  return typeof t == "object" && t !== null ? t : {};
}
function to(t, e) {
  return Object.keys(t).reduce((n, o) => {
    if (o.startsWith("on") && xt(t[o])) {
      const r = t[o];
      n[o] = (...i) => {
        r == null || r(e, ...i);
      };
    } else
      n[o] = t[o];
    return n;
  }, {});
}
const ao = Ur(Jn(["menu.items"], Yn(["default", "items"], ({
  slots: t,
  setSlotParams: e,
  children: n,
  items: o,
  ...r
}) => {
  const {
    items: {
      "menu.items": i
    }
  } = Qn(), s = bt(r.menu), a = typeof r.groupable == "object" || t["groupable.title"], l = eo(r.groupable), c = bt(r.groupable), f = Me(() => {
    if (typeof r.menu == "string")
      return s;
    {
      const g = r.menu || {};
      return (y) => ({
        ...to(g, y),
        items: g.items || Ae(i, {
          clone: !0
        }) || [],
        expandIcon: t["menu.expandIcon"] ? vt({
          slots: t,
          setSlotParams: e,
          key: "menu.expandIcon"
        }, {
          clone: !0
        }) : g.expandIcon,
        overflowedIndicator: t["menu.overflowedIndicator"] ? /* @__PURE__ */ D.jsx(oe, {
          slot: t["menu.overflowedIndicator"]
        }) : g.overflowedIndicator
      });
    }
  }, [s, i, r.menu, e, t]), {
    items: u
  } = Zn(), d = u.items.length > 0 ? u.items : u.default;
  return /* @__PURE__ */ D.jsxs(D.Fragment, {
    children: [/* @__PURE__ */ D.jsx("div", {
      style: {
        display: "none"
      },
      children: n
    }), /* @__PURE__ */ D.jsx(Wn, {
      ...r,
      menu: f,
      items: Me(() => o || Ae(d, {
        clone: !0
      }), [o, d]),
      groupable: a ? {
        ...l,
        title: t["groupable.title"] ? vt({
          slots: t,
          setSlotParams: e,
          key: "groupable.title"
        }) : l.title,
        sort: c || l.sort
      } : r.groupable
    })]
  });
})));
export {
  ao as Conversations,
  ao as default
};
