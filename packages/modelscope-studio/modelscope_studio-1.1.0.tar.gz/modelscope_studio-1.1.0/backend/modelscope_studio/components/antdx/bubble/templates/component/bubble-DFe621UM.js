import { i as Ut, a as Le, r as Gt, g as Kt, w as ce, c as Y, b as qt } from "./Index-csfvhE0b.js";
const R = window.ms_globals.React, h = window.ms_globals.React, Xt = window.ms_globals.React.forwardRef, Nt = window.ms_globals.React.useRef, Vt = window.ms_globals.React.useState, Wt = window.ms_globals.React.useEffect, yt = window.ms_globals.React.useMemo, je = window.ms_globals.ReactDOM.createPortal, Yt = window.ms_globals.internalContext.useContextPropsContext, Ge = window.ms_globals.internalContext.ContextPropsProvider, Qt = window.ms_globals.antd.ConfigProvider, De = window.ms_globals.antd.theme, Jt = window.ms_globals.antd.Avatar, oe = window.ms_globals.antdCssinjs.unit, Me = window.ms_globals.antdCssinjs.token2CSSVar, Ke = window.ms_globals.antdCssinjs.useStyleRegister, Zt = window.ms_globals.antdCssinjs.useCSSVarRegister, en = window.ms_globals.antdCssinjs.createTheme, tn = window.ms_globals.antdCssinjs.useCacheToken, vt = window.ms_globals.antdCssinjs.Keyframes;
var nn = /\s/;
function rn(e) {
  for (var t = e.length; t-- && nn.test(e.charAt(t)); )
    ;
  return t;
}
var on = /^\s+/;
function sn(e) {
  return e && e.slice(0, rn(e) + 1).replace(on, "");
}
var qe = NaN, an = /^[-+]0x[0-9a-f]+$/i, cn = /^0b[01]+$/i, ln = /^0o[0-7]+$/i, un = parseInt;
function Ye(e) {
  if (typeof e == "number")
    return e;
  if (Ut(e))
    return qe;
  if (Le(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = Le(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = sn(e);
  var r = cn.test(e);
  return r || ln.test(e) ? un(e.slice(2), r ? 2 : 8) : an.test(e) ? qe : +e;
}
var Pe = function() {
  return Gt.Date.now();
}, fn = "Expected a function", dn = Math.max, hn = Math.min;
function gn(e, t, r) {
  var o, n, i, s, a, c, l = 0, u = !1, f = !1, d = !0;
  if (typeof e != "function")
    throw new TypeError(fn);
  t = Ye(t) || 0, Le(r) && (u = !!r.leading, f = "maxWait" in r, i = f ? dn(Ye(r.maxWait) || 0, t) : i, d = "trailing" in r ? !!r.trailing : d);
  function S(y) {
    var E = o, M = n;
    return o = n = void 0, l = y, s = e.apply(M, E), s;
  }
  function C(y) {
    return l = y, a = setTimeout(T, t), u ? S(y) : s;
  }
  function g(y) {
    var E = y - c, M = y - l, m = t - E;
    return f ? hn(m, i - M) : m;
  }
  function _(y) {
    var E = y - c, M = y - l;
    return c === void 0 || E >= t || E < 0 || f && M >= i;
  }
  function T() {
    var y = Pe();
    if (_(y))
      return P(y);
    a = setTimeout(T, g(y));
  }
  function P(y) {
    return a = void 0, d && o ? S(y) : (o = n = void 0, s);
  }
  function k() {
    a !== void 0 && clearTimeout(a), l = 0, o = c = n = a = void 0;
  }
  function p() {
    return a === void 0 ? s : P(Pe());
  }
  function b() {
    var y = Pe(), E = _(y);
    if (o = arguments, n = this, c = y, E) {
      if (a === void 0)
        return C(c);
      if (f)
        return clearTimeout(a), a = setTimeout(T, t), S(c);
    }
    return a === void 0 && (a = setTimeout(T, t)), s;
  }
  return b.cancel = k, b.flush = p, b;
}
var St = {
  exports: {}
}, ge = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var pn = h, mn = Symbol.for("react.element"), bn = Symbol.for("react.fragment"), yn = Object.prototype.hasOwnProperty, vn = pn.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Sn = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function xt(e, t, r) {
  var o, n = {}, i = null, s = null;
  r !== void 0 && (i = "" + r), t.key !== void 0 && (i = "" + t.key), t.ref !== void 0 && (s = t.ref);
  for (o in t) yn.call(t, o) && !Sn.hasOwnProperty(o) && (n[o] = t[o]);
  if (e && e.defaultProps) for (o in t = e.defaultProps, t) n[o] === void 0 && (n[o] = t[o]);
  return {
    $$typeof: mn,
    type: e,
    key: i,
    ref: s,
    props: n,
    _owner: vn.current
  };
}
ge.Fragment = bn;
ge.jsx = xt;
ge.jsxs = xt;
St.exports = ge;
var B = St.exports;
const {
  SvelteComponent: xn,
  assign: Qe,
  binding_callbacks: Je,
  check_outros: Cn,
  children: Ct,
  claim_element: _t,
  claim_space: _n,
  component_subscribe: Ze,
  compute_slots: wn,
  create_slot: Tn,
  detach: J,
  element: wt,
  empty: et,
  exclude_internal_props: tt,
  get_all_dirty_from_scope: En,
  get_slot_changes: Mn,
  group_outros: Pn,
  init: On,
  insert_hydration: le,
  safe_not_equal: Rn,
  set_custom_element_data: Tt,
  space: In,
  transition_in: ue,
  transition_out: $e,
  update_slot_base: kn
} = window.__gradio__svelte__internal, {
  beforeUpdate: jn,
  getContext: Ln,
  onDestroy: Dn,
  setContext: $n
} = window.__gradio__svelte__internal;
function nt(e) {
  let t, r;
  const o = (
    /*#slots*/
    e[7].default
  ), n = Tn(
    o,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = wt("svelte-slot"), n && n.c(), this.h();
    },
    l(i) {
      t = _t(i, "SVELTE-SLOT", {
        class: !0
      });
      var s = Ct(t);
      n && n.l(s), s.forEach(J), this.h();
    },
    h() {
      Tt(t, "class", "svelte-1rt0kpf");
    },
    m(i, s) {
      le(i, t, s), n && n.m(t, null), e[9](t), r = !0;
    },
    p(i, s) {
      n && n.p && (!r || s & /*$$scope*/
      64) && kn(
        n,
        o,
        i,
        /*$$scope*/
        i[6],
        r ? Mn(
          o,
          /*$$scope*/
          i[6],
          s,
          null
        ) : En(
          /*$$scope*/
          i[6]
        ),
        null
      );
    },
    i(i) {
      r || (ue(n, i), r = !0);
    },
    o(i) {
      $e(n, i), r = !1;
    },
    d(i) {
      i && J(t), n && n.d(i), e[9](null);
    }
  };
}
function Bn(e) {
  let t, r, o, n, i = (
    /*$$slots*/
    e[4].default && nt(e)
  );
  return {
    c() {
      t = wt("react-portal-target"), r = In(), i && i.c(), o = et(), this.h();
    },
    l(s) {
      t = _t(s, "REACT-PORTAL-TARGET", {
        class: !0
      }), Ct(t).forEach(J), r = _n(s), i && i.l(s), o = et(), this.h();
    },
    h() {
      Tt(t, "class", "svelte-1rt0kpf");
    },
    m(s, a) {
      le(s, t, a), e[8](t), le(s, r, a), i && i.m(s, a), le(s, o, a), n = !0;
    },
    p(s, [a]) {
      /*$$slots*/
      s[4].default ? i ? (i.p(s, a), a & /*$$slots*/
      16 && ue(i, 1)) : (i = nt(s), i.c(), ue(i, 1), i.m(o.parentNode, o)) : i && (Pn(), $e(i, 1, 1, () => {
        i = null;
      }), Cn());
    },
    i(s) {
      n || (ue(i), n = !0);
    },
    o(s) {
      $e(i), n = !1;
    },
    d(s) {
      s && (J(t), J(r), J(o)), e[8](null), i && i.d(s);
    }
  };
}
function rt(e) {
  const {
    svelteInit: t,
    ...r
  } = e;
  return r;
}
function Hn(e, t, r) {
  let o, n, {
    $$slots: i = {},
    $$scope: s
  } = t;
  const a = wn(i);
  let {
    svelteInit: c
  } = t;
  const l = ce(rt(t)), u = ce();
  Ze(e, u, (p) => r(0, o = p));
  const f = ce();
  Ze(e, f, (p) => r(1, n = p));
  const d = [], S = Ln("$$ms-gr-react-wrapper"), {
    slotKey: C,
    slotIndex: g,
    subSlotIndex: _
  } = Kt() || {}, T = c({
    parent: S,
    props: l,
    target: u,
    slot: f,
    slotKey: C,
    slotIndex: g,
    subSlotIndex: _,
    onDestroy(p) {
      d.push(p);
    }
  });
  $n("$$ms-gr-react-wrapper", T), jn(() => {
    l.set(rt(t));
  }), Dn(() => {
    d.forEach((p) => p());
  });
  function P(p) {
    Je[p ? "unshift" : "push"](() => {
      o = p, u.set(o);
    });
  }
  function k(p) {
    Je[p ? "unshift" : "push"](() => {
      n = p, f.set(n);
    });
  }
  return e.$$set = (p) => {
    r(17, t = Qe(Qe({}, t), tt(p))), "svelteInit" in p && r(5, c = p.svelteInit), "$$scope" in p && r(6, s = p.$$scope);
  }, t = tt(t), [o, n, u, f, a, c, s, i, P, k];
}
class zn extends xn {
  constructor(t) {
    super(), On(this, t, Hn, Bn, Rn, {
      svelteInit: 5
    });
  }
}
const ot = window.ms_globals.rerender, Oe = window.ms_globals.tree;
function An(e, t = {}) {
  function r(o) {
    const n = ce(), i = new zn({
      ...o,
      props: {
        svelteInit(s) {
          window.ms_globals.autokey += 1;
          const a = {
            key: window.ms_globals.autokey,
            svelteInstance: n,
            reactComponent: e,
            props: s.props,
            slot: s.slot,
            target: s.target,
            slotIndex: s.slotIndex,
            subSlotIndex: s.subSlotIndex,
            ignore: t.ignore,
            slotKey: s.slotKey,
            nodes: []
          }, c = s.parent ?? Oe;
          return c.nodes = [...c.nodes, a], ot({
            createPortal: je,
            node: Oe
          }), s.onDestroy(() => {
            c.nodes = c.nodes.filter((l) => l.svelteInstance !== n), ot({
              createPortal: je,
              node: Oe
            });
          }), a;
        },
        ...o.props
      }
    });
    return n.set(i), i;
  }
  return new Promise((o) => {
    window.ms_globals.initializePromise.then(() => {
      o(r);
    });
  });
}
const Fn = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function Xn(e) {
  return e ? Object.keys(e).reduce((t, r) => {
    const o = e[r];
    return t[r] = Nn(r, o), t;
  }, {}) : {};
}
function Nn(e, t) {
  return typeof t == "number" && !Fn.includes(e) ? t + "px" : t;
}
function Be(e) {
  const t = [], r = e.cloneNode(!1);
  if (e._reactElement) {
    const n = h.Children.toArray(e._reactElement.props.children).map((i) => {
      if (h.isValidElement(i) && i.props.__slot__) {
        const {
          portals: s,
          clonedElement: a
        } = Be(i.props.el);
        return h.cloneElement(i, {
          ...i.props,
          el: a,
          children: [...h.Children.toArray(i.props.children), ...s]
        });
      }
      return null;
    });
    return n.originalChildren = e._reactElement.props.children, t.push(je(h.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: n
    }), r)), {
      clonedElement: r,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((n) => {
    e.getEventListeners(n).forEach(({
      listener: s,
      type: a,
      useCapture: c
    }) => {
      r.addEventListener(a, s, c);
    });
  });
  const o = Array.from(e.childNodes);
  for (let n = 0; n < o.length; n++) {
    const i = o[n];
    if (i.nodeType === 1) {
      const {
        clonedElement: s,
        portals: a
      } = Be(i);
      t.push(...a), r.appendChild(s);
    } else i.nodeType === 3 && r.appendChild(i.cloneNode());
  }
  return {
    clonedElement: r,
    portals: t
  };
}
function Vn(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const Q = Xt(({
  slot: e,
  clone: t,
  className: r,
  style: o,
  observeAttributes: n
}, i) => {
  const s = Nt(), [a, c] = Vt([]), {
    forceClone: l
  } = Yt(), u = l ? !0 : t;
  return Wt(() => {
    var C;
    if (!s.current || !e)
      return;
    let f = e;
    function d() {
      let g = f;
      if (f.tagName.toLowerCase() === "svelte-slot" && f.children.length === 1 && f.children[0] && (g = f.children[0], g.tagName.toLowerCase() === "react-portal-target" && g.children[0] && (g = g.children[0])), Vn(i, g), r && g.classList.add(...r.split(" ")), o) {
        const _ = Xn(o);
        Object.keys(_).forEach((T) => {
          g.style[T] = _[T];
        });
      }
    }
    let S = null;
    if (u && window.MutationObserver) {
      let g = function() {
        var k, p, b;
        (k = s.current) != null && k.contains(f) && ((p = s.current) == null || p.removeChild(f));
        const {
          portals: T,
          clonedElement: P
        } = Be(e);
        f = P, c(T), f.style.display = "contents", d(), (b = s.current) == null || b.appendChild(f);
      };
      g();
      const _ = gn(() => {
        g(), S == null || S.disconnect(), S == null || S.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: n
        });
      }, 50);
      S = new window.MutationObserver(_), S.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      f.style.display = "contents", d(), (C = s.current) == null || C.appendChild(f);
    return () => {
      var g, _;
      f.style.display = "", (g = s.current) != null && g.contains(f) && ((_ = s.current) == null || _.removeChild(f)), S == null || S.disconnect();
    };
  }, [e, u, r, o, i, n]), h.createElement("react-child", {
    ref: s,
    style: {
      display: "contents"
    }
  }, ...a);
}), Wn = "1.0.5", Un = /* @__PURE__ */ h.createContext({}), Gn = {
  classNames: {},
  styles: {},
  className: "",
  style: {}
}, Kn = (e) => {
  const t = h.useContext(Un);
  return h.useMemo(() => ({
    ...Gn,
    ...t[e]
  }), [t[e]]);
};
function ie() {
  return ie = Object.assign ? Object.assign.bind() : function(e) {
    for (var t = 1; t < arguments.length; t++) {
      var r = arguments[t];
      for (var o in r) ({}).hasOwnProperty.call(r, o) && (e[o] = r[o]);
    }
    return e;
  }, ie.apply(null, arguments);
}
function de() {
  const {
    getPrefixCls: e,
    direction: t,
    csp: r,
    iconPrefixCls: o,
    theme: n
  } = h.useContext(Qt.ConfigContext);
  return {
    theme: n,
    getPrefixCls: e,
    direction: t,
    csp: r,
    iconPrefixCls: o
  };
}
function Et(e) {
  var t = R.useRef();
  t.current = e;
  var r = R.useCallback(function() {
    for (var o, n = arguments.length, i = new Array(n), s = 0; s < n; s++)
      i[s] = arguments[s];
    return (o = t.current) === null || o === void 0 ? void 0 : o.call.apply(o, [t].concat(i));
  }, []);
  return r;
}
function qn(e) {
  if (Array.isArray(e)) return e;
}
function Yn(e, t) {
  var r = e == null ? null : typeof Symbol < "u" && e[Symbol.iterator] || e["@@iterator"];
  if (r != null) {
    var o, n, i, s, a = [], c = !0, l = !1;
    try {
      if (i = (r = r.call(e)).next, t === 0) {
        if (Object(r) !== r) return;
        c = !1;
      } else for (; !(c = (o = i.call(r)).done) && (a.push(o.value), a.length !== t); c = !0) ;
    } catch (u) {
      l = !0, n = u;
    } finally {
      try {
        if (!c && r.return != null && (s = r.return(), Object(s) !== s)) return;
      } finally {
        if (l) throw n;
      }
    }
    return a;
  }
}
function it(e, t) {
  (t == null || t > e.length) && (t = e.length);
  for (var r = 0, o = Array(t); r < t; r++) o[r] = e[r];
  return o;
}
function Qn(e, t) {
  if (e) {
    if (typeof e == "string") return it(e, t);
    var r = {}.toString.call(e).slice(8, -1);
    return r === "Object" && e.constructor && (r = e.constructor.name), r === "Map" || r === "Set" ? Array.from(e) : r === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r) ? it(e, t) : void 0;
  }
}
function Jn() {
  throw new TypeError(`Invalid attempt to destructure non-iterable instance.
In order to be iterable, non-array objects must have a [Symbol.iterator]() method.`);
}
function fe(e, t) {
  return qn(e) || Yn(e, t) || Qn(e, t) || Jn();
}
function Zn() {
  return !!(typeof window < "u" && window.document && window.document.createElement);
}
var st = Zn() ? R.useLayoutEffect : R.useEffect, er = function(t, r) {
  var o = R.useRef(!0);
  st(function() {
    return t(o.current);
  }, r), st(function() {
    return o.current = !1, function() {
      o.current = !0;
    };
  }, []);
};
function N(e) {
  "@babel/helpers - typeof";
  return N = typeof Symbol == "function" && typeof Symbol.iterator == "symbol" ? function(t) {
    return typeof t;
  } : function(t) {
    return t && typeof Symbol == "function" && t.constructor === Symbol && t !== Symbol.prototype ? "symbol" : typeof t;
  }, N(e);
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
var Ae = Symbol.for("react.element"), Fe = Symbol.for("react.portal"), pe = Symbol.for("react.fragment"), me = Symbol.for("react.strict_mode"), be = Symbol.for("react.profiler"), ye = Symbol.for("react.provider"), ve = Symbol.for("react.context"), tr = Symbol.for("react.server_context"), Se = Symbol.for("react.forward_ref"), xe = Symbol.for("react.suspense"), Ce = Symbol.for("react.suspense_list"), _e = Symbol.for("react.memo"), we = Symbol.for("react.lazy"), nr = Symbol.for("react.offscreen"), Mt;
Mt = Symbol.for("react.module.reference");
function H(e) {
  if (typeof e == "object" && e !== null) {
    var t = e.$$typeof;
    switch (t) {
      case Ae:
        switch (e = e.type, e) {
          case pe:
          case be:
          case me:
          case xe:
          case Ce:
            return e;
          default:
            switch (e = e && e.$$typeof, e) {
              case tr:
              case ve:
              case Se:
              case we:
              case _e:
              case ye:
                return e;
              default:
                return t;
            }
        }
      case Fe:
        return t;
    }
  }
}
w.ContextConsumer = ve;
w.ContextProvider = ye;
w.Element = Ae;
w.ForwardRef = Se;
w.Fragment = pe;
w.Lazy = we;
w.Memo = _e;
w.Portal = Fe;
w.Profiler = be;
w.StrictMode = me;
w.Suspense = xe;
w.SuspenseList = Ce;
w.isAsyncMode = function() {
  return !1;
};
w.isConcurrentMode = function() {
  return !1;
};
w.isContextConsumer = function(e) {
  return H(e) === ve;
};
w.isContextProvider = function(e) {
  return H(e) === ye;
};
w.isElement = function(e) {
  return typeof e == "object" && e !== null && e.$$typeof === Ae;
};
w.isForwardRef = function(e) {
  return H(e) === Se;
};
w.isFragment = function(e) {
  return H(e) === pe;
};
w.isLazy = function(e) {
  return H(e) === we;
};
w.isMemo = function(e) {
  return H(e) === _e;
};
w.isPortal = function(e) {
  return H(e) === Fe;
};
w.isProfiler = function(e) {
  return H(e) === be;
};
w.isStrictMode = function(e) {
  return H(e) === me;
};
w.isSuspense = function(e) {
  return H(e) === xe;
};
w.isSuspenseList = function(e) {
  return H(e) === Ce;
};
w.isValidElementType = function(e) {
  return typeof e == "string" || typeof e == "function" || e === pe || e === be || e === me || e === xe || e === Ce || e === nr || typeof e == "object" && e !== null && (e.$$typeof === we || e.$$typeof === _e || e.$$typeof === ye || e.$$typeof === ve || e.$$typeof === Se || e.$$typeof === Mt || e.getModuleId !== void 0);
};
w.typeOf = H;
function rr(e, t) {
  if (N(e) != "object" || !e) return e;
  var r = e[Symbol.toPrimitive];
  if (r !== void 0) {
    var o = r.call(e, t || "default");
    if (N(o) != "object") return o;
    throw new TypeError("@@toPrimitive must return a primitive value.");
  }
  return (t === "string" ? String : Number)(e);
}
function Pt(e) {
  var t = rr(e, "string");
  return N(t) == "symbol" ? t : t + "";
}
function I(e, t, r) {
  return (t = Pt(t)) in e ? Object.defineProperty(e, t, {
    value: r,
    enumerable: !0,
    configurable: !0,
    writable: !0
  }) : e[t] = r, e;
}
function at(e, t) {
  var r = Object.keys(e);
  if (Object.getOwnPropertySymbols) {
    var o = Object.getOwnPropertySymbols(e);
    t && (o = o.filter(function(n) {
      return Object.getOwnPropertyDescriptor(e, n).enumerable;
    })), r.push.apply(r, o);
  }
  return r;
}
function $(e) {
  for (var t = 1; t < arguments.length; t++) {
    var r = arguments[t] != null ? arguments[t] : {};
    t % 2 ? at(Object(r), !0).forEach(function(o) {
      I(e, o, r[o]);
    }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(r)) : at(Object(r)).forEach(function(o) {
      Object.defineProperty(e, o, Object.getOwnPropertyDescriptor(r, o));
    });
  }
  return e;
}
function Te(e, t) {
  if (!(e instanceof t)) throw new TypeError("Cannot call a class as a function");
}
function or(e, t) {
  for (var r = 0; r < t.length; r++) {
    var o = t[r];
    o.enumerable = o.enumerable || !1, o.configurable = !0, "value" in o && (o.writable = !0), Object.defineProperty(e, Pt(o.key), o);
  }
}
function Ee(e, t, r) {
  return t && or(e.prototype, t), Object.defineProperty(e, "prototype", {
    writable: !1
  }), e;
}
function He(e, t) {
  return He = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function(r, o) {
    return r.__proto__ = o, r;
  }, He(e, t);
}
function Ot(e, t) {
  if (typeof t != "function" && t !== null) throw new TypeError("Super expression must either be null or a function");
  e.prototype = Object.create(t && t.prototype, {
    constructor: {
      value: e,
      writable: !0,
      configurable: !0
    }
  }), Object.defineProperty(e, "prototype", {
    writable: !1
  }), t && He(e, t);
}
function he(e) {
  return he = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function(t) {
    return t.__proto__ || Object.getPrototypeOf(t);
  }, he(e);
}
function Rt() {
  try {
    var e = !Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function() {
    }));
  } catch {
  }
  return (Rt = function() {
    return !!e;
  })();
}
function re(e) {
  if (e === void 0) throw new ReferenceError("this hasn't been initialised - super() hasn't been called");
  return e;
}
function ir(e, t) {
  if (t && (N(t) == "object" || typeof t == "function")) return t;
  if (t !== void 0) throw new TypeError("Derived constructors may only return object or undefined");
  return re(e);
}
function It(e) {
  var t = Rt();
  return function() {
    var r, o = he(e);
    if (t) {
      var n = he(this).constructor;
      r = Reflect.construct(o, arguments, n);
    } else r = o.apply(this, arguments);
    return ir(this, r);
  };
}
var kt = /* @__PURE__ */ Ee(function e() {
  Te(this, e);
}), jt = "CALC_UNIT", sr = new RegExp(jt, "g");
function Re(e) {
  return typeof e == "number" ? "".concat(e).concat(jt) : e;
}
var ar = /* @__PURE__ */ function(e) {
  Ot(r, e);
  var t = It(r);
  function r(o, n) {
    var i;
    Te(this, r), i = t.call(this), I(re(i), "result", ""), I(re(i), "unitlessCssVar", void 0), I(re(i), "lowPriority", void 0);
    var s = N(o);
    return i.unitlessCssVar = n, o instanceof r ? i.result = "(".concat(o.result, ")") : s === "number" ? i.result = Re(o) : s === "string" && (i.result = o), i;
  }
  return Ee(r, [{
    key: "add",
    value: function(n) {
      return n instanceof r ? this.result = "".concat(this.result, " + ").concat(n.getResult()) : (typeof n == "number" || typeof n == "string") && (this.result = "".concat(this.result, " + ").concat(Re(n))), this.lowPriority = !0, this;
    }
  }, {
    key: "sub",
    value: function(n) {
      return n instanceof r ? this.result = "".concat(this.result, " - ").concat(n.getResult()) : (typeof n == "number" || typeof n == "string") && (this.result = "".concat(this.result, " - ").concat(Re(n))), this.lowPriority = !0, this;
    }
  }, {
    key: "mul",
    value: function(n) {
      return this.lowPriority && (this.result = "(".concat(this.result, ")")), n instanceof r ? this.result = "".concat(this.result, " * ").concat(n.getResult(!0)) : (typeof n == "number" || typeof n == "string") && (this.result = "".concat(this.result, " * ").concat(n)), this.lowPriority = !1, this;
    }
  }, {
    key: "div",
    value: function(n) {
      return this.lowPriority && (this.result = "(".concat(this.result, ")")), n instanceof r ? this.result = "".concat(this.result, " / ").concat(n.getResult(!0)) : (typeof n == "number" || typeof n == "string") && (this.result = "".concat(this.result, " / ").concat(n)), this.lowPriority = !1, this;
    }
  }, {
    key: "getResult",
    value: function(n) {
      return this.lowPriority || n ? "(".concat(this.result, ")") : this.result;
    }
  }, {
    key: "equal",
    value: function(n) {
      var i = this, s = n || {}, a = s.unit, c = !0;
      return typeof a == "boolean" ? c = a : Array.from(this.unitlessCssVar).some(function(l) {
        return i.result.includes(l);
      }) && (c = !1), this.result = this.result.replace(sr, c ? "px" : ""), typeof this.lowPriority < "u" ? "calc(".concat(this.result, ")") : this.result;
    }
  }]), r;
}(kt), cr = /* @__PURE__ */ function(e) {
  Ot(r, e);
  var t = It(r);
  function r(o) {
    var n;
    return Te(this, r), n = t.call(this), I(re(n), "result", 0), o instanceof r ? n.result = o.result : typeof o == "number" && (n.result = o), n;
  }
  return Ee(r, [{
    key: "add",
    value: function(n) {
      return n instanceof r ? this.result += n.result : typeof n == "number" && (this.result += n), this;
    }
  }, {
    key: "sub",
    value: function(n) {
      return n instanceof r ? this.result -= n.result : typeof n == "number" && (this.result -= n), this;
    }
  }, {
    key: "mul",
    value: function(n) {
      return n instanceof r ? this.result *= n.result : typeof n == "number" && (this.result *= n), this;
    }
  }, {
    key: "div",
    value: function(n) {
      return n instanceof r ? this.result /= n.result : typeof n == "number" && (this.result /= n), this;
    }
  }, {
    key: "equal",
    value: function() {
      return this.result;
    }
  }]), r;
}(kt), lr = function(t, r) {
  var o = t === "css" ? ar : cr;
  return function(n) {
    return new o(n, r);
  };
}, ct = function(t, r) {
  return "".concat([r, t.replace(/([A-Z]+)([A-Z][a-z]+)/g, "$1-$2").replace(/([a-z])([A-Z])/g, "$1-$2")].filter(Boolean).join("-"));
};
function lt(e, t, r, o) {
  var n = $({}, t[e]);
  if (o != null && o.deprecatedTokens) {
    var i = o.deprecatedTokens;
    i.forEach(function(a) {
      var c = fe(a, 2), l = c[0], u = c[1];
      if (n != null && n[l] || n != null && n[u]) {
        var f;
        (f = n[u]) !== null && f !== void 0 || (n[u] = n == null ? void 0 : n[l]);
      }
    });
  }
  var s = $($({}, r), n);
  return Object.keys(s).forEach(function(a) {
    s[a] === t[a] && delete s[a];
  }), s;
}
var Lt = typeof CSSINJS_STATISTIC < "u", ze = !0;
function Xe() {
  for (var e = arguments.length, t = new Array(e), r = 0; r < e; r++)
    t[r] = arguments[r];
  if (!Lt)
    return Object.assign.apply(Object, [{}].concat(t));
  ze = !1;
  var o = {};
  return t.forEach(function(n) {
    if (N(n) === "object") {
      var i = Object.keys(n);
      i.forEach(function(s) {
        Object.defineProperty(o, s, {
          configurable: !0,
          enumerable: !0,
          get: function() {
            return n[s];
          }
        });
      });
    }
  }), ze = !0, o;
}
var ut = {};
function ur() {
}
var fr = function(t) {
  var r, o = t, n = ur;
  return Lt && typeof Proxy < "u" && (r = /* @__PURE__ */ new Set(), o = new Proxy(t, {
    get: function(s, a) {
      if (ze) {
        var c;
        (c = r) === null || c === void 0 || c.add(a);
      }
      return s[a];
    }
  }), n = function(s, a) {
    var c;
    ut[s] = {
      global: Array.from(r),
      component: $($({}, (c = ut[s]) === null || c === void 0 ? void 0 : c.component), a)
    };
  }), {
    token: o,
    keys: r,
    flush: n
  };
};
function ft(e, t, r) {
  if (typeof r == "function") {
    var o;
    return r(Xe(t, (o = t[e]) !== null && o !== void 0 ? o : {}));
  }
  return r ?? {};
}
function dr(e) {
  return e === "js" ? {
    max: Math.max,
    min: Math.min
  } : {
    max: function() {
      for (var r = arguments.length, o = new Array(r), n = 0; n < r; n++)
        o[n] = arguments[n];
      return "max(".concat(o.map(function(i) {
        return oe(i);
      }).join(","), ")");
    },
    min: function() {
      for (var r = arguments.length, o = new Array(r), n = 0; n < r; n++)
        o[n] = arguments[n];
      return "min(".concat(o.map(function(i) {
        return oe(i);
      }).join(","), ")");
    }
  };
}
var hr = 1e3 * 60 * 10, gr = /* @__PURE__ */ function() {
  function e() {
    Te(this, e), I(this, "map", /* @__PURE__ */ new Map()), I(this, "objectIDMap", /* @__PURE__ */ new WeakMap()), I(this, "nextID", 0), I(this, "lastAccessBeat", /* @__PURE__ */ new Map()), I(this, "accessBeat", 0);
  }
  return Ee(e, [{
    key: "set",
    value: function(r, o) {
      this.clear();
      var n = this.getCompositeKey(r);
      this.map.set(n, o), this.lastAccessBeat.set(n, Date.now());
    }
  }, {
    key: "get",
    value: function(r) {
      var o = this.getCompositeKey(r), n = this.map.get(o);
      return this.lastAccessBeat.set(o, Date.now()), this.accessBeat += 1, n;
    }
  }, {
    key: "getCompositeKey",
    value: function(r) {
      var o = this, n = r.map(function(i) {
        return i && N(i) === "object" ? "obj_".concat(o.getObjectID(i)) : "".concat(N(i), "_").concat(i);
      });
      return n.join("|");
    }
  }, {
    key: "getObjectID",
    value: function(r) {
      if (this.objectIDMap.has(r))
        return this.objectIDMap.get(r);
      var o = this.nextID;
      return this.objectIDMap.set(r, o), this.nextID += 1, o;
    }
  }, {
    key: "clear",
    value: function() {
      var r = this;
      if (this.accessBeat > 1e4) {
        var o = Date.now();
        this.lastAccessBeat.forEach(function(n, i) {
          o - n > hr && (r.map.delete(i), r.lastAccessBeat.delete(i));
        }), this.accessBeat = 0;
      }
    }
  }]), e;
}(), dt = new gr();
function pr(e, t) {
  return h.useMemo(function() {
    var r = dt.get(t);
    if (r)
      return r;
    var o = e();
    return dt.set(t, o), o;
  }, t);
}
var mr = function() {
  return {};
};
function br(e) {
  var t = e.useCSP, r = t === void 0 ? mr : t, o = e.useToken, n = e.usePrefix, i = e.getResetStyles, s = e.getCommonStyle, a = e.getCompUnitless;
  function c(d, S, C, g) {
    var _ = Array.isArray(d) ? d[0] : d;
    function T(M) {
      return "".concat(String(_)).concat(M.slice(0, 1).toUpperCase()).concat(M.slice(1));
    }
    var P = (g == null ? void 0 : g.unitless) || {}, k = typeof a == "function" ? a(d) : {}, p = $($({}, k), {}, I({}, T("zIndexPopup"), !0));
    Object.keys(P).forEach(function(M) {
      p[T(M)] = P[M];
    });
    var b = $($({}, g), {}, {
      unitless: p,
      prefixToken: T
    }), y = u(d, S, C, b), E = l(_, C, b);
    return function(M) {
      var m = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : M, O = y(M, m), z = fe(O, 2), L = z[1], A = E(m), v = fe(A, 2), x = v[0], j = v[1];
      return [x, L, j];
    };
  }
  function l(d, S, C) {
    var g = C.unitless, _ = C.injectStyle, T = _ === void 0 ? !0 : _, P = C.prefixToken, k = C.ignore, p = function(E) {
      var M = E.rootCls, m = E.cssVar, O = m === void 0 ? {} : m, z = o(), L = z.realToken;
      return Zt({
        path: [d],
        prefix: O.prefix,
        key: O.key,
        unitless: g,
        ignore: k,
        token: L,
        scope: M
      }, function() {
        var A = ft(d, L, S), v = lt(d, L, A, {
          deprecatedTokens: C == null ? void 0 : C.deprecatedTokens
        });
        return Object.keys(A).forEach(function(x) {
          v[P(x)] = v[x], delete v[x];
        }), v;
      }), null;
    }, b = function(E) {
      var M = o(), m = M.cssVar;
      return [function(O) {
        return T && m ? /* @__PURE__ */ h.createElement(h.Fragment, null, /* @__PURE__ */ h.createElement(p, {
          rootCls: E,
          cssVar: m,
          component: d
        }), O) : O;
      }, m == null ? void 0 : m.key];
    };
    return b;
  }
  function u(d, S, C) {
    var g = arguments.length > 3 && arguments[3] !== void 0 ? arguments[3] : {}, _ = Array.isArray(d) ? d : [d, d], T = fe(_, 1), P = T[0], k = _.join("-"), p = e.layer || {
      name: "antd"
    };
    return function(b) {
      var y = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : b, E = o(), M = E.theme, m = E.realToken, O = E.hashId, z = E.token, L = E.cssVar, A = n(), v = A.rootPrefixCls, x = A.iconPrefixCls, j = r(), F = L ? "css" : "js", W = pr(function() {
        var X = /* @__PURE__ */ new Set();
        return L && Object.keys(g.unitless || {}).forEach(function(G) {
          X.add(Me(G, L.prefix)), X.add(Me(G, ct(P, L.prefix)));
        }), lr(F, X);
      }, [F, P, L == null ? void 0 : L.prefix]), U = dr(F), K = U.max, Z = U.min, ee = {
        theme: M,
        token: z,
        hashId: O,
        nonce: function() {
          return j.nonce;
        },
        clientOnly: g.clientOnly,
        layer: p,
        // antd is always at top of styles
        order: g.order || -999
      };
      typeof i == "function" && Ke($($({}, ee), {}, {
        clientOnly: !1,
        path: ["Shared", v]
      }), function() {
        return i(z, {
          prefix: {
            rootPrefixCls: v,
            iconPrefixCls: x
          },
          csp: j
        });
      });
      var te = Ke($($({}, ee), {}, {
        path: [k, b, x]
      }), function() {
        if (g.injectStyle === !1)
          return [];
        var X = fr(z), G = X.token, Ht = X.flush, q = ft(P, m, C), zt = ".".concat(b), Ve = lt(P, m, q, {
          deprecatedTokens: g.deprecatedTokens
        });
        L && q && N(q) === "object" && Object.keys(q).forEach(function(Ue) {
          q[Ue] = "var(".concat(Me(Ue, ct(P, L.prefix)), ")");
        });
        var We = Xe(G, {
          componentCls: zt,
          prefixCls: b,
          iconCls: ".".concat(x),
          antCls: ".".concat(v),
          calc: W,
          // @ts-ignore
          max: K,
          // @ts-ignore
          min: Z
        }, L ? q : Ve), At = S(We, {
          hashId: O,
          prefixCls: b,
          rootPrefixCls: v,
          iconPrefixCls: x
        });
        Ht(P, Ve);
        var Ft = typeof s == "function" ? s(We, b, y, g.resetFont) : null;
        return [g.resetStyle === !1 ? null : Ft, At];
      });
      return [te, O];
    };
  }
  function f(d, S, C) {
    var g = arguments.length > 3 && arguments[3] !== void 0 ? arguments[3] : {}, _ = u(d, S, C, $({
      resetStyle: !1,
      // Sub Style should default after root one
      order: -998
    }, g)), T = function(k) {
      var p = k.prefixCls, b = k.rootCls, y = b === void 0 ? p : b;
      return _(p, y), null;
    };
    return T;
  }
  return {
    genStyleHooks: c,
    genSubStyleComponent: f,
    genComponentStyleHook: u
  };
}
const D = Math.round;
function Ie(e, t) {
  const r = e.replace(/^[^(]*\((.*)/, "$1").replace(/\).*/, "").match(/\d*\.?\d+%?/g) || [], o = r.map((n) => parseFloat(n));
  for (let n = 0; n < 3; n += 1)
    o[n] = t(o[n] || 0, r[n] || "", n);
  return r[3] ? o[3] = r[3].includes("%") ? o[3] / 100 : o[3] : o[3] = 1, o;
}
const ht = (e, t, r) => r === 0 ? e : e / 100;
function ne(e, t) {
  const r = t || 255;
  return e > r ? r : e < 0 ? 0 : e;
}
class V {
  constructor(t) {
    I(this, "isValid", !0), I(this, "r", 0), I(this, "g", 0), I(this, "b", 0), I(this, "a", 1), I(this, "_h", void 0), I(this, "_s", void 0), I(this, "_l", void 0), I(this, "_v", void 0), I(this, "_max", void 0), I(this, "_min", void 0), I(this, "_brightness", void 0);
    function r(o) {
      return o[0] in t && o[1] in t && o[2] in t;
    }
    if (t) if (typeof t == "string") {
      let n = function(i) {
        return o.startsWith(i);
      };
      const o = t.trim();
      /^#?[A-F\d]{3,8}$/i.test(o) ? this.fromHexString(o) : n("rgb") ? this.fromRgbString(o) : n("hsl") ? this.fromHslString(o) : (n("hsv") || n("hsb")) && this.fromHsvString(o);
    } else if (t instanceof V)
      this.r = t.r, this.g = t.g, this.b = t.b, this.a = t.a, this._h = t._h, this._s = t._s, this._l = t._l, this._v = t._v;
    else if (r("rgb"))
      this.r = ne(t.r), this.g = ne(t.g), this.b = ne(t.b), this.a = typeof t.a == "number" ? ne(t.a, 1) : 1;
    else if (r("hsl"))
      this.fromHsl(t);
    else if (r("hsv"))
      this.fromHsv(t);
    else
      throw new Error("@ant-design/fast-color: unsupported input " + JSON.stringify(t));
  }
  // ======================= Setter =======================
  setR(t) {
    return this._sc("r", t);
  }
  setG(t) {
    return this._sc("g", t);
  }
  setB(t) {
    return this._sc("b", t);
  }
  setA(t) {
    return this._sc("a", t, 1);
  }
  setHue(t) {
    const r = this.toHsv();
    return r.h = t, this._c(r);
  }
  // ======================= Getter =======================
  /**
   * Returns the perceived luminance of a color, from 0-1.
   * @see http://www.w3.org/TR/2008/REC-WCAG20-20081211/#relativeluminancedef
   */
  getLuminance() {
    function t(i) {
      const s = i / 255;
      return s <= 0.03928 ? s / 12.92 : Math.pow((s + 0.055) / 1.055, 2.4);
    }
    const r = t(this.r), o = t(this.g), n = t(this.b);
    return 0.2126 * r + 0.7152 * o + 0.0722 * n;
  }
  getHue() {
    if (typeof this._h > "u") {
      const t = this.getMax() - this.getMin();
      t === 0 ? this._h = 0 : this._h = D(60 * (this.r === this.getMax() ? (this.g - this.b) / t + (this.g < this.b ? 6 : 0) : this.g === this.getMax() ? (this.b - this.r) / t + 2 : (this.r - this.g) / t + 4));
    }
    return this._h;
  }
  getSaturation() {
    if (typeof this._s > "u") {
      const t = this.getMax() - this.getMin();
      t === 0 ? this._s = 0 : this._s = t / this.getMax();
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
  darken(t = 10) {
    const r = this.getHue(), o = this.getSaturation();
    let n = this.getLightness() - t / 100;
    return n < 0 && (n = 0), this._c({
      h: r,
      s: o,
      l: n,
      a: this.a
    });
  }
  lighten(t = 10) {
    const r = this.getHue(), o = this.getSaturation();
    let n = this.getLightness() + t / 100;
    return n > 1 && (n = 1), this._c({
      h: r,
      s: o,
      l: n,
      a: this.a
    });
  }
  /**
   * Mix the current color a given amount with another color, from 0 to 100.
   * 0 means no mixing (return current color).
   */
  mix(t, r = 50) {
    const o = this._c(t), n = r / 100, i = (a) => (o[a] - this[a]) * n + this[a], s = {
      r: D(i("r")),
      g: D(i("g")),
      b: D(i("b")),
      a: D(i("a") * 100) / 100
    };
    return this._c(s);
  }
  /**
   * Mix the color with pure white, from 0 to 100.
   * Providing 0 will do nothing, providing 100 will always return white.
   */
  tint(t = 10) {
    return this.mix({
      r: 255,
      g: 255,
      b: 255,
      a: 1
    }, t);
  }
  /**
   * Mix the color with pure black, from 0 to 100.
   * Providing 0 will do nothing, providing 100 will always return black.
   */
  shade(t = 10) {
    return this.mix({
      r: 0,
      g: 0,
      b: 0,
      a: 1
    }, t);
  }
  onBackground(t) {
    const r = this._c(t), o = this.a + r.a * (1 - this.a), n = (i) => D((this[i] * this.a + r[i] * r.a * (1 - this.a)) / o);
    return this._c({
      r: n("r"),
      g: n("g"),
      b: n("b"),
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
  equals(t) {
    return this.r === t.r && this.g === t.g && this.b === t.b && this.a === t.a;
  }
  clone() {
    return this._c(this);
  }
  // ======================= Format =======================
  toHexString() {
    let t = "#";
    const r = (this.r || 0).toString(16);
    t += r.length === 2 ? r : "0" + r;
    const o = (this.g || 0).toString(16);
    t += o.length === 2 ? o : "0" + o;
    const n = (this.b || 0).toString(16);
    if (t += n.length === 2 ? n : "0" + n, typeof this.a == "number" && this.a >= 0 && this.a < 1) {
      const i = D(this.a * 255).toString(16);
      t += i.length === 2 ? i : "0" + i;
    }
    return t;
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
    const t = this.getHue(), r = D(this.getSaturation() * 100), o = D(this.getLightness() * 100);
    return this.a !== 1 ? `hsla(${t},${r}%,${o}%,${this.a})` : `hsl(${t},${r}%,${o}%)`;
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
  _sc(t, r, o) {
    const n = this.clone();
    return n[t] = ne(r, o), n;
  }
  _c(t) {
    return new this.constructor(t);
  }
  getMax() {
    return typeof this._max > "u" && (this._max = Math.max(this.r, this.g, this.b)), this._max;
  }
  getMin() {
    return typeof this._min > "u" && (this._min = Math.min(this.r, this.g, this.b)), this._min;
  }
  fromHexString(t) {
    const r = t.replace("#", "");
    function o(n, i) {
      return parseInt(r[n] + r[i || n], 16);
    }
    r.length < 6 ? (this.r = o(0), this.g = o(1), this.b = o(2), this.a = r[3] ? o(3) / 255 : 1) : (this.r = o(0, 1), this.g = o(2, 3), this.b = o(4, 5), this.a = r[6] ? o(6, 7) / 255 : 1);
  }
  fromHsl({
    h: t,
    s: r,
    l: o,
    a: n
  }) {
    if (this._h = t % 360, this._s = r, this._l = o, this.a = typeof n == "number" ? n : 1, r <= 0) {
      const d = D(o * 255);
      this.r = d, this.g = d, this.b = d;
    }
    let i = 0, s = 0, a = 0;
    const c = t / 60, l = (1 - Math.abs(2 * o - 1)) * r, u = l * (1 - Math.abs(c % 2 - 1));
    c >= 0 && c < 1 ? (i = l, s = u) : c >= 1 && c < 2 ? (i = u, s = l) : c >= 2 && c < 3 ? (s = l, a = u) : c >= 3 && c < 4 ? (s = u, a = l) : c >= 4 && c < 5 ? (i = u, a = l) : c >= 5 && c < 6 && (i = l, a = u);
    const f = o - l / 2;
    this.r = D((i + f) * 255), this.g = D((s + f) * 255), this.b = D((a + f) * 255);
  }
  fromHsv({
    h: t,
    s: r,
    v: o,
    a: n
  }) {
    this._h = t % 360, this._s = r, this._v = o, this.a = typeof n == "number" ? n : 1;
    const i = D(o * 255);
    if (this.r = i, this.g = i, this.b = i, r <= 0)
      return;
    const s = t / 60, a = Math.floor(s), c = s - a, l = D(o * (1 - r) * 255), u = D(o * (1 - r * c) * 255), f = D(o * (1 - r * (1 - c)) * 255);
    switch (a) {
      case 0:
        this.g = f, this.b = l;
        break;
      case 1:
        this.r = u, this.b = l;
        break;
      case 2:
        this.r = l, this.b = f;
        break;
      case 3:
        this.r = l, this.g = u;
        break;
      case 4:
        this.r = f, this.g = l;
        break;
      case 5:
      default:
        this.g = l, this.b = u;
        break;
    }
  }
  fromHsvString(t) {
    const r = Ie(t, ht);
    this.fromHsv({
      h: r[0],
      s: r[1],
      v: r[2],
      a: r[3]
    });
  }
  fromHslString(t) {
    const r = Ie(t, ht);
    this.fromHsl({
      h: r[0],
      s: r[1],
      l: r[2],
      a: r[3]
    });
  }
  fromRgbString(t) {
    const r = Ie(t, (o, n) => (
      // Convert percentage to number. e.g. 50% -> 128
      n.includes("%") ? D(o / 100 * 255) : o
    ));
    this.r = r[0], this.g = r[1], this.b = r[2], this.a = r[3];
  }
}
const yr = {
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
}, vr = Object.assign(Object.assign({}, yr), {
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
function ke(e) {
  return e >= 0 && e <= 255;
}
function se(e, t) {
  const {
    r,
    g: o,
    b: n,
    a: i
  } = new V(e).toRgb();
  if (i < 1)
    return e;
  const {
    r: s,
    g: a,
    b: c
  } = new V(t).toRgb();
  for (let l = 0.01; l <= 1; l += 0.01) {
    const u = Math.round((r - s * (1 - l)) / l), f = Math.round((o - a * (1 - l)) / l), d = Math.round((n - c * (1 - l)) / l);
    if (ke(u) && ke(f) && ke(d))
      return new V({
        r: u,
        g: f,
        b: d,
        a: Math.round(l * 100) / 100
      }).toRgbString();
  }
  return new V({
    r,
    g: o,
    b: n,
    a: 1
  }).toRgbString();
}
var Sr = function(e, t) {
  var r = {};
  for (var o in e) Object.prototype.hasOwnProperty.call(e, o) && t.indexOf(o) < 0 && (r[o] = e[o]);
  if (e != null && typeof Object.getOwnPropertySymbols == "function") for (var n = 0, o = Object.getOwnPropertySymbols(e); n < o.length; n++)
    t.indexOf(o[n]) < 0 && Object.prototype.propertyIsEnumerable.call(e, o[n]) && (r[o[n]] = e[o[n]]);
  return r;
};
function xr(e) {
  const {
    override: t
  } = e, r = Sr(e, ["override"]), o = Object.assign({}, t);
  Object.keys(vr).forEach((d) => {
    delete o[d];
  });
  const n = Object.assign(Object.assign({}, r), o), i = 480, s = 576, a = 768, c = 992, l = 1200, u = 1600;
  if (n.motion === !1) {
    const d = "0s";
    n.motionDurationFast = d, n.motionDurationMid = d, n.motionDurationSlow = d;
  }
  return Object.assign(Object.assign(Object.assign({}, n), {
    // ============== Background ============== //
    colorFillContent: n.colorFillSecondary,
    colorFillContentHover: n.colorFill,
    colorFillAlter: n.colorFillQuaternary,
    colorBgContainerDisabled: n.colorFillTertiary,
    // ============== Split ============== //
    colorBorderBg: n.colorBgContainer,
    colorSplit: se(n.colorBorderSecondary, n.colorBgContainer),
    // ============== Text ============== //
    colorTextPlaceholder: n.colorTextQuaternary,
    colorTextDisabled: n.colorTextQuaternary,
    colorTextHeading: n.colorText,
    colorTextLabel: n.colorTextSecondary,
    colorTextDescription: n.colorTextTertiary,
    colorTextLightSolid: n.colorWhite,
    colorHighlight: n.colorError,
    colorBgTextHover: n.colorFillSecondary,
    colorBgTextActive: n.colorFill,
    colorIcon: n.colorTextTertiary,
    colorIconHover: n.colorText,
    colorErrorOutline: se(n.colorErrorBg, n.colorBgContainer),
    colorWarningOutline: se(n.colorWarningBg, n.colorBgContainer),
    // Font
    fontSizeIcon: n.fontSizeSM,
    // Line
    lineWidthFocus: n.lineWidth * 3,
    // Control
    lineWidth: n.lineWidth,
    controlOutlineWidth: n.lineWidth * 2,
    // Checkbox size and expand icon size
    controlInteractiveSize: n.controlHeight / 2,
    controlItemBgHover: n.colorFillTertiary,
    controlItemBgActive: n.colorPrimaryBg,
    controlItemBgActiveHover: n.colorPrimaryBgHover,
    controlItemBgActiveDisabled: n.colorFill,
    controlTmpOutline: n.colorFillQuaternary,
    controlOutline: se(n.colorPrimaryBg, n.colorBgContainer),
    lineType: n.lineType,
    borderRadius: n.borderRadius,
    borderRadiusXS: n.borderRadiusXS,
    borderRadiusSM: n.borderRadiusSM,
    borderRadiusLG: n.borderRadiusLG,
    fontWeightStrong: 600,
    opacityLoading: 0.65,
    linkDecoration: "none",
    linkHoverDecoration: "none",
    linkFocusDecoration: "none",
    controlPaddingHorizontal: 12,
    controlPaddingHorizontalSM: 8,
    paddingXXS: n.sizeXXS,
    paddingXS: n.sizeXS,
    paddingSM: n.sizeSM,
    padding: n.size,
    paddingMD: n.sizeMD,
    paddingLG: n.sizeLG,
    paddingXL: n.sizeXL,
    paddingContentHorizontalLG: n.sizeLG,
    paddingContentVerticalLG: n.sizeMS,
    paddingContentHorizontal: n.sizeMS,
    paddingContentVertical: n.sizeSM,
    paddingContentHorizontalSM: n.size,
    paddingContentVerticalSM: n.sizeXS,
    marginXXS: n.sizeXXS,
    marginXS: n.sizeXS,
    marginSM: n.sizeSM,
    margin: n.size,
    marginMD: n.sizeMD,
    marginLG: n.sizeLG,
    marginXL: n.sizeXL,
    marginXXL: n.sizeXXL,
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
    screenMDMax: c - 1,
    screenLG: c,
    screenLGMin: c,
    screenLGMax: l - 1,
    screenXL: l,
    screenXLMin: l,
    screenXLMax: u - 1,
    screenXXL: u,
    screenXXLMin: u,
    boxShadowPopoverArrow: "2px 2px 5px rgba(0, 0, 0, 0.05)",
    boxShadowCard: `
      0 1px 2px -2px ${new V("rgba(0, 0, 0, 0.16)").toRgbString()},
      0 3px 6px 0 ${new V("rgba(0, 0, 0, 0.12)").toRgbString()},
      0 5px 12px 4px ${new V("rgba(0, 0, 0, 0.09)").toRgbString()}
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
const Cr = {
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
}, _r = {
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
}, wr = en(De.defaultAlgorithm), Tr = {
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
}, Dt = (e, t, r) => {
  const o = r.getDerivativeToken(e), {
    override: n,
    ...i
  } = t;
  let s = {
    ...o,
    override: n
  };
  return s = xr(s), i && Object.entries(i).forEach(([a, c]) => {
    const {
      theme: l,
      ...u
    } = c;
    let f = u;
    l && (f = Dt({
      ...s,
      ...u
    }, {
      override: u
    }, l)), s[a] = f;
  }), s;
};
function Er() {
  const {
    token: e,
    hashed: t,
    theme: r = wr,
    override: o,
    cssVar: n
  } = h.useContext(De._internalContext), [i, s, a] = tn(r, [De.defaultSeed, e], {
    salt: `${Wn}-${t || ""}`,
    override: o,
    getComputedToken: Dt,
    cssVar: n && {
      prefix: n.prefix,
      key: n.key,
      unitless: Cr,
      ignore: _r,
      preserve: Tr
    }
  });
  return [r, a, t ? s : "", i, n];
}
const {
  genStyleHooks: Mr,
  genComponentStyleHook: Zr,
  genSubStyleComponent: eo
} = br({
  usePrefix: () => {
    const {
      getPrefixCls: e,
      iconPrefixCls: t
    } = de();
    return {
      iconPrefixCls: t,
      rootPrefixCls: e()
    };
  },
  useToken: () => {
    const [e, t, r, o, n] = Er();
    return {
      theme: e,
      realToken: t,
      hashId: r,
      token: o,
      cssVar: n
    };
  },
  useCSP: () => {
    const {
      csp: e
    } = de();
    return e ?? {};
  },
  layer: {
    name: "antdx",
    dependencies: ["antd"]
  }
});
var Pr = `accept acceptCharset accessKey action allowFullScreen allowTransparency
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
    summary tabIndex target title type useMap value width wmode wrap`, Or = `onCopy onCut onPaste onCompositionEnd onCompositionStart onCompositionUpdate onKeyDown
    onKeyPress onKeyUp onFocus onBlur onChange onInput onSubmit onClick onContextMenu onDoubleClick
    onDrag onDragEnd onDragEnter onDragExit onDragLeave onDragOver onDragStart onDrop onMouseDown
    onMouseEnter onMouseLeave onMouseMove onMouseOut onMouseOver onMouseUp onSelect onTouchCancel
    onTouchEnd onTouchMove onTouchStart onScroll onWheel onAbort onCanPlay onCanPlayThrough
    onDurationChange onEmptied onEncrypted onEnded onError onLoadedData onLoadedMetadata
    onLoadStart onPause onPlay onPlaying onProgress onRateChange onSeeked onSeeking onStalled onSuspend onTimeUpdate onVolumeChange onWaiting onLoad onError`, Rr = "".concat(Pr, " ").concat(Or).split(/[\s\n]+/), Ir = "aria-", kr = "data-";
function gt(e, t) {
  return e.indexOf(t) === 0;
}
function jr(e) {
  var t = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : !1, r;
  t === !1 ? r = {
    aria: !0,
    data: !0,
    attr: !0
  } : t === !0 ? r = {
    aria: !0
  } : r = $({}, t);
  var o = {};
  return Object.keys(e).forEach(function(n) {
    // Aria
    (r.aria && (n === "role" || gt(n, Ir)) || // Data
    r.data && gt(n, kr) || // Attr
    r.attr && Rr.includes(n)) && (o[n] = e[n]);
  }), o;
}
function ae(e) {
  return typeof e == "string";
}
const Lr = (e, t, r, o) => {
  const [n, i] = R.useState(""), [s, a] = R.useState(1), c = t && ae(e);
  return er(() => {
    i(e), !c && ae(e) ? a(e.length) : ae(e) && ae(n) && e.indexOf(n) !== 0 && a(1);
  }, [e]), R.useEffect(() => {
    if (c && s < e.length) {
      const u = setTimeout(() => {
        a((f) => f + r);
      }, o);
      return () => {
        clearTimeout(u);
      };
    }
  }, [s, t, e]), [c ? e.slice(0, s) : e, c && s < e.length];
};
function Dr(e) {
  return R.useMemo(() => {
    if (!e)
      return [!1, 0, 0, null];
    let t = {
      step: 1,
      interval: 50,
      // set default suffix is empty
      suffix: null
    };
    return typeof e == "object" && (t = {
      ...t,
      ...e
    }), [!0, t.step, t.interval, t.suffix];
  }, [e]);
}
const $r = ({
  prefixCls: e
}) => /* @__PURE__ */ h.createElement("span", {
  className: `${e}-dot`
}, /* @__PURE__ */ h.createElement("i", {
  className: `${e}-dot-item`,
  key: "item-1"
}), /* @__PURE__ */ h.createElement("i", {
  className: `${e}-dot-item`,
  key: "item-2"
}), /* @__PURE__ */ h.createElement("i", {
  className: `${e}-dot-item`,
  key: "item-3"
})), Br = (e) => {
  const {
    componentCls: t,
    paddingSM: r,
    padding: o
  } = e;
  return {
    [t]: {
      [`${t}-content`]: {
        // Shared: filled, outlined, shadow
        "&-filled,&-outlined,&-shadow": {
          padding: `${oe(r)} ${oe(o)}`,
          borderRadius: e.borderRadiusLG
        },
        // Filled:
        "&-filled": {
          backgroundColor: e.colorFillContent
        },
        // Outlined:
        "&-outlined": {
          border: `1px solid ${e.colorBorderSecondary}`
        },
        // Shadow:
        "&-shadow": {
          boxShadow: e.boxShadowTertiary
        }
      }
    }
  };
}, Hr = (e) => {
  const {
    componentCls: t,
    fontSize: r,
    lineHeight: o,
    paddingSM: n,
    padding: i,
    calc: s
  } = e, a = s(r).mul(o).div(2).add(n).equal(), c = `${t}-content`;
  return {
    [t]: {
      [c]: {
        // round:
        "&-round": {
          borderRadius: {
            _skip_check_: !0,
            value: a
          },
          paddingInline: s(i).mul(1.25).equal()
        }
      },
      // corner:
      [`&-start ${c}-corner`]: {
        borderStartStartRadius: e.borderRadiusXS
      },
      [`&-end ${c}-corner`]: {
        borderStartEndRadius: e.borderRadiusXS
      }
    }
  };
}, zr = (e) => {
  const {
    componentCls: t,
    padding: r
  } = e;
  return {
    [`${t}-list`]: {
      display: "flex",
      flexDirection: "column",
      gap: r,
      overflowY: "auto"
    }
  };
}, Ar = new vt("loadingMove", {
  "0%": {
    transform: "translateY(0)"
  },
  "10%": {
    transform: "translateY(4px)"
  },
  "20%": {
    transform: "translateY(0)"
  },
  "30%": {
    transform: "translateY(-4px)"
  },
  "40%": {
    transform: "translateY(0)"
  }
}), Fr = new vt("cursorBlink", {
  "0%": {
    opacity: 1
  },
  "50%": {
    opacity: 0
  },
  "100%": {
    opacity: 1
  }
}), Xr = (e) => {
  const {
    componentCls: t,
    fontSize: r,
    lineHeight: o,
    paddingSM: n,
    colorText: i,
    calc: s
  } = e;
  return {
    [t]: {
      display: "flex",
      columnGap: n,
      [`&${t}-end`]: {
        justifyContent: "end",
        flexDirection: "row-reverse",
        [`& ${t}-content-wrapper`]: {
          alignItems: "flex-end"
        }
      },
      [`&${t}-rtl`]: {
        direction: "rtl"
      },
      [`&${t}-typing ${t}-content:last-child::after`]: {
        content: '"|"',
        fontWeight: 900,
        userSelect: "none",
        opacity: 1,
        marginInlineStart: "0.1em",
        animationName: Fr,
        animationDuration: "0.8s",
        animationIterationCount: "infinite",
        animationTimingFunction: "linear"
      },
      // ============================ Avatar =============================
      [`& ${t}-avatar`]: {
        display: "inline-flex",
        justifyContent: "center",
        alignSelf: "flex-start"
      },
      // ======================== Header & Footer ========================
      [`& ${t}-header, & ${t}-footer`]: {
        fontSize: r,
        lineHeight: o,
        color: e.colorText
      },
      [`& ${t}-header`]: {
        marginBottom: e.paddingXXS
      },
      [`& ${t}-footer`]: {
        marginTop: n
      },
      // =========================== Content =============================
      [`& ${t}-content-wrapper`]: {
        flex: "auto",
        display: "flex",
        flexDirection: "column",
        alignItems: "flex-start",
        minWidth: 0,
        maxWidth: "100%"
      },
      [`& ${t}-content`]: {
        position: "relative",
        boxSizing: "border-box",
        minWidth: 0,
        maxWidth: "100%",
        color: i,
        fontSize: e.fontSize,
        lineHeight: e.lineHeight,
        minHeight: s(n).mul(2).add(s(o).mul(r)).equal(),
        wordBreak: "break-word",
        [`& ${t}-dot`]: {
          position: "relative",
          height: "100%",
          display: "flex",
          alignItems: "center",
          columnGap: e.marginXS,
          padding: `0 ${oe(e.paddingXXS)}`,
          "&-item": {
            backgroundColor: e.colorPrimary,
            borderRadius: "100%",
            width: 4,
            height: 4,
            animationName: Ar,
            animationDuration: "2s",
            animationIterationCount: "infinite",
            animationTimingFunction: "linear",
            "&:nth-child(1)": {
              animationDelay: "0s"
            },
            "&:nth-child(2)": {
              animationDelay: "0.2s"
            },
            "&:nth-child(3)": {
              animationDelay: "0.4s"
            }
          }
        }
      }
    }
  };
}, Nr = () => ({}), $t = Mr("Bubble", (e) => {
  const t = Xe(e, {});
  return [Xr(t), zr(t), Br(t), Hr(t)];
}, Nr), Bt = /* @__PURE__ */ h.createContext({}), Vr = (e, t) => {
  const {
    prefixCls: r,
    className: o,
    rootClassName: n,
    style: i,
    classNames: s = {},
    styles: a = {},
    avatar: c,
    placement: l = "start",
    loading: u = !1,
    loadingRender: f,
    typing: d,
    content: S = "",
    messageRender: C,
    variant: g = "filled",
    shape: _,
    onTypingComplete: T,
    header: P,
    footer: k,
    ...p
  } = e, {
    onUpdate: b
  } = h.useContext(Bt), y = h.useRef(null);
  h.useImperativeHandle(t, () => ({
    nativeElement: y.current
  }));
  const {
    direction: E,
    getPrefixCls: M
  } = de(), m = M("bubble", r), O = Kn("bubble"), [z, L, A, v] = Dr(d), [x, j] = Lr(S, z, L, A);
  h.useEffect(() => {
    b == null || b();
  }, [x]);
  const F = h.useRef(!1);
  h.useEffect(() => {
    !j && !u ? F.current || (F.current = !0, T == null || T()) : F.current = !1;
  }, [j, u]);
  const [W, U, K] = $t(m), Z = Y(m, n, O.className, o, U, K, `${m}-${l}`, {
    [`${m}-rtl`]: E === "rtl",
    [`${m}-typing`]: j && !u && !C && !v
  }), ee = /* @__PURE__ */ h.isValidElement(c) ? c : /* @__PURE__ */ h.createElement(Jt, c), te = C ? C(x) : x;
  let X;
  u ? X = f ? f() : /* @__PURE__ */ h.createElement($r, {
    prefixCls: m
  }) : X = /* @__PURE__ */ h.createElement(h.Fragment, null, te, j && v);
  let G = /* @__PURE__ */ h.createElement("div", {
    style: {
      ...O.styles.content,
      ...a.content
    },
    className: Y(`${m}-content`, `${m}-content-${g}`, _ && `${m}-content-${_}`, O.classNames.content, s.content)
  }, X);
  return (P || k) && (G = /* @__PURE__ */ h.createElement("div", {
    className: `${m}-content-wrapper`
  }, P && /* @__PURE__ */ h.createElement("div", {
    className: Y(`${m}-header`, O.classNames.header, s.header),
    style: {
      ...O.styles.header,
      ...a.header
    }
  }, P), G, k && /* @__PURE__ */ h.createElement("div", {
    className: Y(`${m}-footer`, O.classNames.footer, s.footer),
    style: {
      ...O.styles.footer,
      ...a.footer
    }
  }, k))), W(/* @__PURE__ */ h.createElement("div", ie({
    style: {
      ...O.style,
      ...i
    },
    className: Z
  }, p, {
    ref: y
  }), c && /* @__PURE__ */ h.createElement("div", {
    style: {
      ...O.styles.avatar,
      ...a.avatar
    },
    className: Y(`${m}-avatar`, O.classNames.avatar, s.avatar)
  }, ee), G));
}, Ne = /* @__PURE__ */ h.forwardRef(Vr);
function Wr(e) {
  const [t, r] = h.useState(e.length), o = h.useMemo(() => e.slice(0, t), [e, t]), n = h.useMemo(() => {
    const s = o[o.length - 1];
    return s ? s.key : null;
  }, [o]);
  h.useEffect(() => {
    var s;
    if (!(o.length && o.every((a, c) => {
      var l;
      return a.key === ((l = e[c]) == null ? void 0 : l.key);
    }))) {
      if (o.length === 0)
        r(1);
      else
        for (let a = 0; a < o.length; a += 1)
          if (o[a].key !== ((s = e[a]) == null ? void 0 : s.key)) {
            r(a);
            break;
          }
    }
  }, [e]);
  const i = Et((s) => {
    s === n && r(t + 1);
  });
  return [o, i];
}
function Ur(e, t) {
  const r = R.useCallback((o) => typeof t == "function" ? t(o) : t ? t[o.role] || {} : {}, [t]);
  return R.useMemo(() => (e || []).map((o, n) => {
    const i = o.key ?? `preset_${n}`;
    return {
      ...r(o),
      ...o,
      key: i
    };
  }), [e, r]);
}
const Gr = 1, Kr = (e, t) => {
  const {
    prefixCls: r,
    rootClassName: o,
    className: n,
    items: i,
    autoScroll: s = !0,
    roles: a,
    ...c
  } = e, l = jr(c, {
    attr: !0,
    aria: !0
  }), u = R.useRef(null), f = R.useRef({}), {
    getPrefixCls: d
  } = de(), S = d("bubble", r), C = `${S}-list`, [g, _, T] = $t(S), [P, k] = R.useState(!1);
  R.useEffect(() => (k(!0), () => {
    k(!1);
  }), []);
  const p = Ur(i, a), [b, y] = Wr(p), [E, M] = R.useState(!0), [m, O] = R.useState(0), z = (v) => {
    const x = v.target;
    M(x.scrollHeight - Math.abs(x.scrollTop) - x.clientHeight <= Gr);
  };
  R.useEffect(() => {
    s && u.current && E && u.current.scrollTo({
      top: u.current.scrollHeight
    });
  }, [m]), R.useEffect(() => {
    var v;
    if (s) {
      const x = (v = b[b.length - 2]) == null ? void 0 : v.key, j = f.current[x];
      if (j) {
        const {
          nativeElement: F
        } = j, {
          top: W,
          bottom: U
        } = F.getBoundingClientRect(), {
          top: K,
          bottom: Z
        } = u.current.getBoundingClientRect();
        W < Z && U > K && (O((te) => te + 1), M(!0));
      }
    }
  }, [b.length]), R.useImperativeHandle(t, () => ({
    nativeElement: u.current,
    scrollTo: ({
      key: v,
      offset: x,
      behavior: j = "smooth",
      block: F
    }) => {
      if (typeof x == "number")
        u.current.scrollTo({
          top: x,
          behavior: j
        });
      else if (v !== void 0) {
        const W = f.current[v];
        if (W) {
          const U = b.findIndex((K) => K.key === v);
          M(U === b.length - 1), W.nativeElement.scrollIntoView({
            behavior: j,
            block: F
          });
        }
      }
    }
  }));
  const L = Et(() => {
    s && O((v) => v + 1);
  }), A = R.useMemo(() => ({
    onUpdate: L
  }), []);
  return g(/* @__PURE__ */ R.createElement(Bt.Provider, {
    value: A
  }, /* @__PURE__ */ R.createElement("div", ie({}, l, {
    className: Y(C, o, n, _, T, {
      [`${C}-reach-end`]: E
    }),
    ref: u,
    onScroll: z
  }), b.map(({
    key: v,
    ...x
  }) => /* @__PURE__ */ R.createElement(Ne, ie({}, x, {
    key: v,
    ref: (j) => {
      j ? f.current[v] = j : delete f.current[v];
    },
    typing: P ? x.typing : !1,
    onTypingComplete: () => {
      var j;
      (j = x.onTypingComplete) == null || j.call(x), y(v);
    }
  }))))));
}, qr = /* @__PURE__ */ R.forwardRef(Kr);
Ne.List = qr;
function Yr(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function Qr(e, t = !1) {
  try {
    if (qt(e))
      return e;
    if (t && !Yr(e))
      return;
    if (typeof e == "string") {
      let r = e.trim();
      return r.startsWith(";") && (r = r.slice(1)), r.endsWith(";") && (r = r.slice(0, -1)), new Function(`return (...args) => (${r})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function pt(e, t) {
  return yt(() => Qr(e, t), [e, t]);
}
function mt(e, t) {
  return e ? /* @__PURE__ */ B.jsx(Q, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function bt({
  key: e,
  slots: t,
  targets: r
}, o) {
  return t[e] ? (...n) => r ? r.map((i, s) => /* @__PURE__ */ B.jsx(Ge, {
    params: n,
    forceClone: !0,
    children: mt(i, {
      clone: !0,
      ...o
    })
  }, s)) : /* @__PURE__ */ B.jsx(Ge, {
    params: n,
    forceClone: !0,
    children: mt(t[e], {
      clone: !0,
      ...o
    })
  }) : void 0;
}
const to = An(({
  loadingRender: e,
  messageRender: t,
  slots: r,
  setSlotParams: o,
  children: n,
  ...i
}) => {
  const s = pt(e), a = pt(t), c = yt(() => {
    var l, u;
    return r.avatar ? /* @__PURE__ */ B.jsx(Q, {
      slot: r.avatar
    }) : r["avatar.icon"] || r["avatar.src"] ? {
      ...i.avatar || {},
      icon: r["avatar.icon"] ? /* @__PURE__ */ B.jsx(Q, {
        slot: r["avatar.icon"]
      }) : (l = i.avatar) == null ? void 0 : l.icon,
      src: r["avatar.src"] ? /* @__PURE__ */ B.jsx(Q, {
        slot: r["avatar.src"]
      }) : (u = i.avatar) == null ? void 0 : u.src
    } : i.avatar;
  }, [i.avatar, r]);
  return /* @__PURE__ */ B.jsxs(B.Fragment, {
    children: [/* @__PURE__ */ B.jsx("div", {
      style: {
        display: "none"
      },
      children: n
    }), /* @__PURE__ */ B.jsx(Ne, {
      ...i,
      avatar: c,
      content: r.content ? /* @__PURE__ */ B.jsx(Q, {
        slot: r.content
      }) : i.content,
      footer: r.footer ? /* @__PURE__ */ B.jsx(Q, {
        slot: r.footer
      }) : i.footer,
      loadingRender: r.loadingRender ? bt({
        slots: r,
        setSlotParams: o,
        key: "loadingRender"
      }) : s,
      messageRender: r.messageRender ? bt({
        slots: r,
        setSlotParams: o,
        key: "messageRender"
      }) : a
    })]
  });
});
export {
  to as Bubble,
  to as default
};
